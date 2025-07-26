import os
import subprocess
from tqdm import tqdm

def executar_ffmpeg(video_path, audio_path, output_path):
    """
    Combina um arquivo de vídeo (.mp4) sem som com um arquivo de áudio (.m4a)
    gerando um novo vídeo com som, utilizando o FFmpeg. Exibe uma barra de progresso.
    """
    # Comando do FFmpeg: copia o vídeo e codifica o áudio para AAC.
    comando = [
        "ffmpeg",
        "-i", video_path,      # arquivo de vídeo de entrada
        "-i", audio_path,      # arquivo de áudio de entrada
        "-c:v", "copy",        # copia o stream de vídeo sem re-encode
        "-c:a", "aac",         # codifica o áudio em AAC
        "-y",                  # sobrescreve o arquivo de saída, se existir
        output_path            # caminho do arquivo de saída
    ]

    # Executa o comando e atualiza uma barra de progresso com cada linha do stderr.
    with subprocess.Popen(
        comando,
        stderr=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        universal_newlines=True
    ) as proc:
        for _ in tqdm(proc.stderr, desc="Processando", unit="linhas", ncols=80):
            pass

    print(f"\nProcesso concluído! Arquivo gerado em: {output_path}")

def converter_ts_para_mp4(input_ts, output_mp4):
    """
    Converte um arquivo .ts para .mp4 utilizando o FFmpeg, fazendo somente remux
    (cópia dos fluxos), sem re-encode, garantindo maior velocidade.
    """
    comando = [
        "ffmpeg",
        "-i", input_ts,
        "-c", "copy",
        "-y",            # sobrescreve se o arquivo de saída já existir
        output_mp4
    ]
    subprocess.run(comando, check=True)

def menu_combinar():
    """
    Menu para combinar vídeos (.mp4) e áudios (.m4a). Após cada operação,
    pergunta se deseja repetir ou voltar ao menu principal.
    """
    while True:
        # Entrada dos nomes dos arquivos
        video_file = input("Digite o nome do arquivo de VÍDEO (ex.: video.mp4): ").strip()
        audio_file = input("Digite o nome do arquivo de ÁUDIO (ex.: audio.m4a): ").strip()
        output_file = input("Digite o nome do ARQUIVO FINAL (ex.: final.mp4): ").strip()

        # Verifica a existência dos arquivos
        if not os.path.exists(video_file):
            print(f"ERRO: O arquivo de vídeo '{video_file}' não foi encontrado.")
            continue

        if not os.path.exists(audio_file):
            print(f"ERRO: O arquivo de áudio '{audio_file}' não foi encontrado.")
            continue

        # Cria uma pasta baseada no nome do arquivo final (sem extensão)
        folder_name, _ = os.path.splitext(output_file)
        if not folder_name:
            folder_name = "saida"
        os.makedirs(folder_name, exist_ok=True)

        final_path = os.path.join(folder_name, output_file)

        # Executa a combinação utilizando FFmpeg
        try:
            executar_ffmpeg(video_file, audio_file, final_path)
        except Exception as e:
            print(f"ERRO ao processar: {e}")

        # Pergunta se deseja repetir a operação ou voltar ao menu principal
        escolha = input("Deseja combinar outro par de arquivos? (S para sim / M para voltar ao menu): ").strip().lower()
        if escolha == "m":
            break

def menu_converter_ts():
    """
    Menu para converter arquivos .ts em .mp4 (remux). Após cada conversão,
    pergunta se deseja repetir a operação ou voltar ao menu principal.
    """
    while True:
        # Solicita o caminho da pasta onde estão os arquivos .ts
        ts_folder = input("Caminho onde estão os vídeos .ts (ex.: D:\\videos_ts): ").strip()
        if not os.path.isdir(ts_folder):
            print(f"ERRO: O caminho '{ts_folder}' não é uma pasta válida.")
            escolha = input("Deseja tentar novamente? (S para sim / M para voltar ao menu): ").strip().lower()
            if escolha == "m":
                break
            continue

        # Solicita o nome do arquivo .ts
        ts_name = input("Nome do arquivo .ts (ex.: video.ts): ").strip()
        ts_path = os.path.join(ts_folder, ts_name)
        if not os.path.exists(ts_path):
            print(f"ERRO: O arquivo '{ts_path}' não foi encontrado.")
            escolha = input("Deseja tentar novamente? (S para sim / M para voltar ao menu): ").strip().lower()
            if escolha == "m":
                break
            continue

        # Obtém o diretório do script e cria uma subpasta baseada no nome do arquivo (sem extensão)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        base_name, _ = os.path.splitext(ts_name)
        output_folder = os.path.join(script_dir, base_name)
        os.makedirs(output_folder, exist_ok=True)

        mp4_name = base_name + ".mp4"
        mp4_path = os.path.join(output_folder, mp4_name)

        # Realiza a conversão (remux) de .ts para .mp4
        try:
            converter_ts_para_mp4(ts_path, mp4_path)
            print("Conversão concluída com sucesso!")
            print(f"Arquivo gerado: {mp4_path}")
        except subprocess.CalledProcessError as e:
            print(f"ERRO na conversão: {e}")

        # Pergunta se deseja repetir a conversão ou voltar ao menu principal
        escolha = input("Deseja converter outro arquivo .ts? (S para sim / M para voltar ao menu): ").strip().lower()
        if escolha == "m":
            break

def exibir_menu_principal():
    """
    Exibe o menu principal e direciona para a funcionalidade escolhida.
    """
    while True:
        print("\n======================================================")
        print(" ")
        print("Bem-vindo ao Pirate Script, (by \033]8;;https://t.me/yMusashi\033\\@yMusashi\033]8;;\033\\)")
        print("Com ele você pode baixar vídeos bloqueados do Google Drive")
        print("Obs.: caso não tenha o ffmpeg instalado, baixe-o\nem https://ffmpeg.org/download.html e adicione-o ao PATH")
        print(" ")
        print("Antes de começar, certifique-se de que os arquivos .mp4 e .m4a\nestão na mesma pasta deste script.")
        print(" ")
        print("Antes desse script ser necessário, você precisa dos arquivos .mp4\n e .m4a do vídeo que você quer baixar, para consegui-los, assista\na esse vídeo: https://youtube.com/watch?v=vm-yL-HCAd4&t")
        print(" ")
        print("Este script possui as seguintes funções:")
        print("> 1º - Combinar arquivos .mp4 (sem som) com .m4a para gerar um .mp4 com som")
        print("> 2º - Converter arquivos .ts para .mp4 (remux, sem re-encode)")
        print("> Sair/Fechar (digite 'end')")
        print(" ")
        print("______________________________________________________")
        print(" ")
        opcao = input("Qual operação você deseja iniciar? (1/2/end): ").strip().lower()

        if opcao == "1":
            menu_combinar()
        elif opcao == "2":
            menu_converter_ts()
        elif opcao == "end":
            print("Encerrando o script... Até a próxima!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    exibir_menu_principal()
