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
- Os 14 temas, favoritos e configurações continuam no mesmo pacote de aplicativo.
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

## Glass Pro — versão 2.9.21

Ative em **Temas → Glass Pro · iPhone 18**. Composição abstrata original bordô e azul-gelo,
painéis de vidro, três aparências de ícones, relógio grande e modos dia/noite.
A cápsula de bateria/conexão e os widgets mostram dados reais do Android; toque para abrir
os ajustes correspondentes. O calendário usa a data do aparelho. O dock permite escolher
até quatro aplicativos em **Personalizar tema → Escolher aplicativos do dock** e tem uma
preferência separada dos favoritos antigos. A rolagem continua em Ajustes.

Os 12 temas anteriores foram preservados. Tema independente inspirado no
[iPhone 18 Pro](https://www.apple.com/newsroom/2026/09/apple-debuts-iphone-18-pro-and-iphone-18-pro-max/)
e na linguagem visual Liquid Glass; o sistema continua sendo Android.
Compilação, assinatura e 245 verificações aprovadas; teste em aparelho físico pendente.

## Eve Future — versão 2.9.22

Novo 14º tema em **Temas → Eve Future · Mobilidade aérea**. Arte conceitual original
inspirada no [eVTOL da Eve](https://www.eveairmobility.com/evtol/) ligado à Embraer:
aeronave sobre uma metrópole brasileira futurista e um vertiporto iluminado.

Rotas luminosas, pequenos veículos e radar são uma simulação visual local. A cápsula
de bateria e conexão mostra dados reais do aparelho. Os ícones principais usam o símbolo
Embraer; os nomes maiores e miniícones originais continuam identificando cada aplicativo.

A rotina de modo noite é ativada por padrão, somente no tema Eve Future: noite entre
22h e 6h, usando o horário local do celular. O botão de sol/lua passa para modo manual;
a rotina pode ser reativada em Personalizar tema ou na Central Eve Future. A automação
acompanha mudanças de hora/fuso e a volta ao aplicativo, sem alarmes ou serviços novos.
A central também oferece atalhos para conexões, brilho e economia de bateria. Esses
atalhos abrem os controles do Android; não alteram o aparelho sem sua interação.

Em Personalizar tema é possível desativar as rotas ou o radar, ativar os widgets de
bateria/calendário e visualizar a arte sem ícones. Os efeitos pausam fora do início,
com movimentos reduzidos e durante economia de bateria. A aeronave principal da arte
é estática; o radar, as rotas e os pequenos veículos são animados. Não há telemetria
ou controle de aeronaves reais. Tema independente, sem vínculo oficial com as empresas.

Os 13 temas anteriores e o atualizador foram preservados. Sem novas permissões.
Compilação, assinatura e 334 verificações aprovadas; teste em aparelho físico pendente.

## Corinthians — versão 2.9.23

O gavião faz uma volta completa pela torcida, em ordem: canto do fundo à esquerda,
canto do fundo à direita, canto da frente à direita e canto da frente à esquerda.
Depois, passa novamente pela arquibancada do fundo e sai de cena. A câmera acompanha
o percurso, respeitando as bordas da imagem em telas altas ou largas.

O voo continua com 22 segundos e se repete a cada 60 segundos de tempo visível.
A espiada começa aos 36 segundos, dura 6,5 segundos e alterna as laterais a cada ciclo,
exatamente como antes. O relógio pausa ao sair do início. Arte da Neo Química Arena,
torcida, bandeiras, luzes, confetes, batimento das asas e animação da espiada foram preservados.
Todos os 14 temas continuam disponíveis. Sem novas permissões ou alterações no atualizador.

Compilação, assinatura e 340 verificações aprovadas. A geometria da câmera foi conferida
em cinco formatos de tela e dois formatos de imagem. Teste visual em aparelho físico pendente.

## Corinthians — versão 2.9.24

Novo voo em profundidade: o gavião surge pequeno na arquibancada distante da outra ponta,
desce sobre o gramado, passa junto ao gol próximo e vira na direção do observador.
Ele cresce por perspectiva, atravessa para a frente dos ícones na aproximação final e
sai acima da tela, como se passasse pela lente do celular. A câmera tem deslocamento,
zoom e inclinação mais discretos para manter a arena estável.

O voo usa seis poses desenhadas, com vista em três quartos e frontal, alternando planadas
longas e batidas curtas das asas. Pivôs na cabeça alinham as poses. As camadas do estádio
e da aproximação compartilham a mesma projeção, evitando um salto na transição.
A vista frontal termina em planada. Uma sombra discreta acompanha parte da passagem baixa.

A aproximação é uma animação local com sprites e perspectiva sobre a arte da arena;
não é vídeo ou modelo tridimensional completo. A camada diante dos ícones não recebe
toques e usa o mesmo relógio do estádio. Não há um segundo temporizador de animação.

Mantidos os 22 segundos de voo a cada minuto de tempo visível e a espiada aos 36 segundos,
por 6,5 segundos, com os lados alternados. A arte e a animação da espiada não mudaram.
Torcida, bandeiras, luzes, confetes, todos os 14 temas e permissões anteriores preservados.
Compilação, assinatura e 356 verificações aprovadas; teste visual no celular pendente.
