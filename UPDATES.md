# Atualizações TodaArt3D

Este repositório público distribui **somente APKs de instalação e seus catálogos**.
Não publique chaves de assinatura, senhas, dados pessoais ou arquivos de manutenção.

## Camada Zero

- Pacote: `br.com.camadazero.todaart3d`.
- Catálogo: `apps/br.com.camadazero.todaart3d.json`.
- O aplicativo consulta o catálogo a cada seis horas quando o Android permite o trabalho.
- Por padrão, baixa somente em redes sem cobrança, normalmente Wi-Fi.
- Downloads são conferidos por tamanho, SHA-256, pacote, versão crescente e certificado
  igual ao aplicativo instalado. O Android confirma a instalação.
- Os 12 temas, favoritos e configurações continuam no mesmo pacote de aplicativo.
- É necessário instalar a versão 2.9.20 ou posterior uma vez para receber esse recurso.
- Em **Ajustes → Atualizações do Camada Zero**, é possível desativar a busca,
  permitir outras redes, verificar agora ou instalar o APK baixado.
- Se as notificações estiverem bloqueadas, a atualização continua acessível nos ajustes.
- O Android pode adiar o trabalho por economia de bateria ou restrições do fabricante.

## Publicar uma versão

1. Compilar e assinar localmente com a mesma chave do aplicativo anterior.
2. Verificar o pacote, versão, certificado, tamanho e hash SHA-256.
3. Enviar **apenas o APK** a um link temporário autorizado no tmpfiles.org.
4. Criar ou atualizar `publish.json` com pacote, slug, versão, código, tamanho,
   hash, endereço temporário em `source`, título e notas da versão.
5. O workflow `Publicar aplicativos TodaArt3D` confere o arquivo, cria uma Release
   permanente e somente então publica o catálogo correspondente.
6. Conferir o resultado em Actions e baixar novamente o APK da Release para verificar.

O link temporário precisa continuar válido até a publicação terminar. Os aplicativos
baixam sempre a cópia permanente do GitHub, nunca o link temporário.

## Outros aplicativos

Cada aplicativo precisa receber seu próprio atualizador, preservar seu identificador e
sua chave de assinatura, e ter um catálogo `apps/IDENTIFICADOR.DO.PACOTE.json`.
A criação deste repositório não modifica automaticamente APKs já instalados.
A estrutura de publicação aceita outros pacotes; só publique aplicativos autorizados.
Não use esta estrutura para atualizar apps de terceiros.
