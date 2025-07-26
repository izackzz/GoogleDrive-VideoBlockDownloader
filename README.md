# GoogleDrive-VideoBlockDownloader

Este script foi criado para auxiliar usuários que precisam juntar arquivos de vídeo e áudio baixados separadamente do Google Drive, especialmente em situações onde o download direto do vídeo está bloqueado.

## 🎯 Objetivo

A principal finalidade desta ferramenta é resolver o problema de vídeos sem som que ocorrem ao baixar conteúdo do Google Drive de forma não convencional. Quando um vídeo tem o download restrito, uma das alternativas é capturar os fluxos de vídeo e áudio separadamente através da aba "Network" do navegador. Este script automatiza o processo de unir esses arquivos, resultando em um vídeo completo e com som.

## ✨ Funcionalidades

O script oferece um menu interativo com as seguintes opções:

1.  **Combinar Vídeo e Áudio:**

      * Une um arquivo de vídeo `.mp4` (sem som) com seu respectivo arquivo de áudio `.m4a`.
      * Gera um novo arquivo `.mp4` com o vídeo e o áudio sincronizados.
      * Exibe uma barra de progresso durante o processo.

2.  **Converter .ts para .mp4:**

      * Converte arquivos de vídeo no formato `.ts` para o formato `.mp4`.
      * A conversão é feita através de *remux*, o que significa que os dados de vídeo e áudio são copiados sem re-codificação, garantindo um processo extremamente rápido e sem perda de qualidade.

## 📋 Pré-requisitos

  * **FFmpeg:** É essencial ter o FFmpeg instalado e configurado nas variáveis de ambiente (PATH) do seu sistema para que o script funcione.
      * Você pode baixá-lo em [ffmpeg.org/download.html](https://ffmpeg.org/download.html).

## 🚀 Como Usar

1.  **Preparação:**

      * Coloque os arquivos de vídeo (`.mp4` ou `.ts`) e áudio (`.m4a`) na mesma pasta onde o script está localizado.
      * O script que ensina como obter os arquivos de vídeo e áudio separadamente pode ser encontrado neste [tutorial em vídeo](https://www.youtube.com/watch?v=RF7gJ7ar0-8).

2.  **Execução:**

      * Execute o script Python no seu terminal.
      * Um menu principal será exibido, perguntando qual operação você deseja realizar.

3.  **Opções do Menu:**

      * **Digite `1`** para combinar um vídeo `.mp4` com um áudio `.m4a`. O script pedirá os nomes dos arquivos de entrada e o nome desejado para o arquivo final.
      * **Digite `2`** para converter um arquivo `.ts` para `.mp4`. O script solicitará o caminho e o nome do arquivo `.ts`.
      * **Digite `end`** para fechar o programa.

O arquivo final será salvo em uma nova pasta, criada com o mesmo nome do arquivo de saída para manter a organização.

---

**by [@yMusashi](https://t.me/yMusashi) | [@Prometheust](https://t.me/Prometheust)**
