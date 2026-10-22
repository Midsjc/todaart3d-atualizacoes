"""Publish only reviewed installation APKs. No signing key is needed on GitHub."""
import base64
import hashlib
import http.cookiejar
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import urllib.parse
import urllib.request
import zipfile

MAX_BYTES = 150 * 1024 * 1024
REPOSITORY = 'Midsjc/todaart3d-atualizacoes'


def validate(d):
    assert re.fullmatch(r'[a-z][a-z0-9_]*(?:\.[a-z][a-z0-9_]*)+', d['package'])
    assert re.fullmatch(r'[a-z0-9-]+', d['slug'])
    assert re.fullmatch(r'[0-9]+(?:\.[0-9]+){1,3}', d['versionName'])
    assert isinstance(d['versionCode'], int) and 0 < d['versionCode'] < 2100000000
    assert isinstance(d['bytes'], int) and 1024 <= d['bytes'] <= MAX_BYTES
    assert re.fullmatch(r'[0-9a-f]{64}', d['sha256'])
    u = urllib.parse.urlsplit(d['source'])
    assert u.scheme == 'https' and u.hostname == 'tmpfiles.org' and u.netloc == 'tmpfiles.org'
    assert not u.query and not u.fragment and re.fullmatch(r'/[A-Za-z0-9]+/[A-Za-z0-9._-]+\.apk', u.path)


class HTTPSRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        u = urllib.parse.urlsplit(newurl)
        if u.scheme != 'https' or u.hostname != 'tmpfiles.org' or u.netloc != 'tmpfiles.org':
            raise ValueError('Unexpected download redirect')
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def download(d, dest):
    opener = urllib.request.build_opener(HTTPSRedirect(), urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    with opener.open(d['source'], timeout=30) as response:
        page = response.read(512000).decode('utf-8')
    match = re.search(r'class="download" href="([^"]+)"', page)
    if not match:
        raise ValueError('Temporary APK link expired')
    direct = match[1]
    u = urllib.parse.urlsplit(direct)
    if u.scheme != 'https' or u.netloc != 'tmpfiles.org':
        raise ValueError('Unexpected APK host')
    total = 0
    digest = hashlib.sha256()
    with opener.open(direct, timeout=60) as response, dest.open('wb') as output:
        while chunk := response.read(1024 * 1024):
            total += len(chunk)
            if total > d['bytes']:
                raise ValueError('APK is larger than declared')
            output.write(chunk)
            digest.update(chunk)
    assert total == d['bytes'] and digest.hexdigest() == d['sha256'], 'APK checksum mismatch'
    with zipfile.ZipFile(dest) as archive:
        assert archive.testzip() is None and 'AndroidManifest.xml' in archive.namelist()
        assert not any(n.endswith(('.p12', '.jks', '.pem', '.key')) or 'password.txt' in n for n in archive.namelist())


def gh(*args):
    return subprocess.check_output(['gh', *args], text=True).strip()


def main():
    if os.environ.get('GH_REPO') != REPOSITORY:
        raise ValueError('Wrong publishing repository')
    d = json.loads(Path('publish.json').read_text())
    validate(d)
    tag = d['slug'] + '-v' + d['versionName']
    name = d['slug'] + '-' + d['versionName'] + '.apk'
    feed = {k: d[k] for k in ('package', 'versionName', 'versionCode', 'sha256', 'bytes')}
    feed['url'] = f'https://github.com/{REPOSITORY}/releases/download/{tag}/{name}'
    feedpath = 'apps/' + d['package'] + '.json'
    old = None
    # Only a missing file is an acceptable first publication; permission/server errors fail.
    result = subprocess.run(['gh', 'api', f'repos/{REPOSITORY}/contents/{feedpath}'], capture_output=True, text=True)
    if result.returncode == 0:
        old = json.loads(result.stdout)
        previous = json.loads(base64.b64decode(old['content']))
        if d['versionCode'] <= previous['versionCode']:
            raise ValueError('Version code must increase')
    elif '404' not in result.stderr:
        raise RuntimeError(result.stderr)
    with tempfile.TemporaryDirectory() as temporary:
        dest = Path(temporary) / name
        download(d, dest)
        # Releases are immutable: never replace an existing APK or reuse an old tag.
        gh('release', 'create', tag, str(dest), '--title', d.get('title', tag),
           '--notes', d.get('notes', 'Atualização do aplicativo TodaArt3D.'), '--target', 'main')
    payload = {'message': 'Publicar catálogo ' + tag,
               'content': base64.b64encode((json.dumps(feed, indent=2) + '\n').encode()).decode(),
               'branch': 'main'}
    if old:
        payload['sha'] = old['sha']
    payloadpath = Path(os.environ.get('RUNNER_TEMP', tempfile.gettempdir())) / 'feed-payload.json'
    payloadpath.write_text(json.dumps(payload))
    gh('api', '--method', 'PUT', f'repos/{REPOSITORY}/contents/{feedpath}', '--input', str(payloadpath))
    print('Publicado:', feed['url'])


if __name__ == '__main__':
    main()
