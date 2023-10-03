# Biblioteca que fazem o reconhecimento de keywords do Python para Robot
from cgitb import text
from os import replace
from re import T
from tkinter.messagebox import NO
from pyaudio import Stream
from robot.api.deco import keyword
from selenium.webdriver.chrome import options
from selenium.webdriver.common import action_chains

def reCaptcha():

    #importação de arquivo com as ações do mouse
    from support.mouse import click_mouse1, click_mouse2, click_mouse3, click_mouse4, click_mouse5

    # Importação de time para Sleep.
    import time

    # Importação de biblioteca do sistema
    import os

    # Bibliotecas para transcrição de áudio em texto e auxiliares
    # INSTALAR AS BIBLIOTECAS ABAIXO -> É NECESSÁRIO INSTALAR NA ORDEM ESPECIFICADA
    # 1. pip install NumPy
    # 2. pip install pipwin
    # 3. pipwin install pyaudio
    # 4. pip install wave
    # 5. pip install pyautogui -> Para auxílio na utilização de Keys
    # 6. pip install google-api-python-client
    # 7. pip install monotonic -> Instalar apenas se o código der erro na transcrição do áudio.
    # 8. pip install speechrecognition -> Interpretador de fala
    # 9. pip install pynput

    # Transcrição de áudio em Texto
    import speech_recognition as sr

    # Conversção de metadados
    from speech_recognition import AudioData
    import os

    # Bibliotecas de linguagem
    import pyaudio

    # Biblioteca para gravação de frequências
    import wave

    # Biblioteca necessária para a utilização dos recursos de áudio (python)
    import pyautogui
    
    # Biblioteca de digitação (para digitar o texto do áudio no campo especificado).
    import pynput
    from pynput.keyboard import Key, Controller

    # *********************************************************************
    # Caso o capctcha não passe direto o código irá rodar o script abaixo.
    # *********************************************************************
    
    # Ações com o mouse
    # Click_mouse1() apertado para sair do campo do reCaptcha (caso haja)
    time.sleep(1)
    click_mouse1()
    time.sleep(2)

    # Clica no reCapcha novamente
    #click_mouse1()
    #time.sleep(1)
    click_mouse2()
    time.sleep(2)

    # Exclui o arquivo de áudio do diretório, caso haja.
    try:
        os.remove('audio.wav')
        os.remove('texto.txt')
    except OSError:
        pass

    # GRAVAÇÃO DE AUDIO

    # Nome do arquivo de áudio com a terminação padrão "wav".
    arquivo_audio = 'audio.wav'
    
    # Clica no audio online para fazer a gravação
    click_mouse3()
    
    # **********
    # IMPORTANTE
    # **********

    # É necessário habilitar o "MIXAGEM ESTÉREO" como opção padrão de gravação em seu computador.
    # Para fazer isso, entre em "Alterar sons do sistema" -> Gravação -> Habilitar "Mixagem Estéreo" como dispositivo padrão (de preferência, desabilite os outros microfones).
    # É ncessário que a opção "Alto-falantes" em "REPRODUÇÃO" esteja habilitada com o volume de 60+ para que não hajam problemas de reconhecimento de fala.

    chunk = 2048                        # Define o tamanho de cada pedaço de áudio em 2048
    formato = pyaudio.paInt16           # Formata o arquivo em 16 bits
    canais = 2                          # Número de canais para o áudio
    fs = 44100                          # Grava em 44100 por segundo
    tempo = 6                           # Tempo de gravação
    
    p = pyaudio.PyAudio()               # Cria a porta de áudio Pyaudio

    # Abre uma gravação com os valores definidos acima:
    stream = p.open(format=formato,
                channels = canais,
                rate = fs,
                frames_per_buffer = chunk,
                input = True)
    frames = []

    # Faz a gravação em um arquivo
    for i in range(0, int(fs / chunk * tempo)):
        data = stream.read(chunk)
        frames.append(data)

    # Encerra a gravação
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Define os dados do arquivo WAV
    file = wave.open(arquivo_audio, 'wb')
    file.setnchannels(canais)
    file.setsampwidth(p.get_sample_size(formato))
    file.setframerate(fs)

    # Escreve e fecha o arquivo
    file.writeframes(b''.join(frames))
    file.close()
    time.sleep(2)

    # **************************************************************************
    # Finalização da gravação de áudio -> Início da tradução do áudio para texto
    # **************************************************************************

    # Cria um teclado para digitação sem necessidade de clicar em um elemento específico -> Biblioteca pynput:
    teclado = Controller()

    # Iniciação do Recognizer para transcriçaõ de áudio em texto
    r = sr.Recognizer()

    # Abertura do arquivo criado com o caminho absoluto(caminho diferente em outros computadores). 
    # Essencial deixar o caminho absoluto para não ocorrer erros->> Coloque o caminho da pasta principal do projeto
    with sr.AudioFile('C:/Users/Luã Viana/Documents/Conteúdo para Repasse/POC - ROBOT/Portal - Robot/audio.wav') as source:

        # Definição de ártifices para redução de ruído
        r.energy_threshold = 400
        r.pause_threshold = 1.2
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.30
        r.dynamic_energy_ratio = 1.5

        # Definição do áudio sem ruído e transcrição para texto com recognize_google.
        audio = r.record(source)
        texto = r.recognize_google(audio, language='en-US')

        # O áudio, por vezes, é arquivado em formato de lista. Para transformar em string é necessário fazer o passo abaixo:
        texto = ''.join(texto)

        # Caso o texto seja diferente de nulo e "alternativefinal"(mensagem de erro do recognize_google),
        # Ele irá anotar o texto em um bloco de notas para validação. Caso contrário, ele irá refazer o passo de tradução
        # Com um parametro chamado "Show_all=True", para mostrar o texto completo do arquivo sem necessidade de mostrar o erro anterior.
        if texto != "" or texto != "alternativefinal":

            # Abre um bloco de notas para digitação do texto:
            #->> Coloque o caminho da pasta principal do projeto
            with open('C:/Users/Luã Viana/Documents/Conteúdo para Repasse/POC - ROBOT/Portal - Robot/texto.txt', 'w+') as escrita:
                
                # Escreve o texto em um bloco de notas para validação
                escrita.write(texto)
                time.sleep(1)

                # Clica no campo de digitação do texto
                click_mouse4()
                time.sleep(1)

            # Digita o texto adquirido na tradução.    
            teclado.type(texto)
        else:
            #->> Coloque o caminho da pasta principal do projeto
            with sr.AudioFile('C:/Users/Luã Viana/Documents/Conteúdo para Repasse/POC - ROBOT/Portal - Robot/audio.wav') as source:
                
                # Definição de ártifices para redução de ruído
                r.energy_threshold = 400
                r.pause_threshold = 1.2
                r.dynamic_energy_threshold = True
                r.dynamic_energy_adjustment_damping = 0.30
                r.dynamic_energy_ratio = 1.5
                
                # Definição do áudio sem "noise" e transcrição para texto com recognize_google.
                # Diferença que este código em questão apresenta "Show_all=True", para mostrar todo o conteúdo traduzido.
                audio = r.record(source)
                texto = r.recognize_google(audio, language='en-US', show_all=True)

                # O áudio, por vezes, é arquivado em formato de lista. Para transformar em string é necessário fazer o passo abaixo:
                texto = ''.join(texto)

                # Abre um bloco de notas para digitação do texto:
                #->> Coloque o caminho da pasta principal do projeto
                with open('C:/Users/Luã Viana/Documents/Conteúdo para Repasse/POC - ROBOT/Portal - Robot/texto.txt', 'w+') as escrita:
                    
                    # Escreve o texto em um bloco de notas para validação
                    escrita.write(texto)
                    time.sleep(1)

                    # Clica no campo de digitação do texto
                    click_mouse4()
                    time.sleep(1)
                
                # Digita o texto adquirido na tradução
                teclado.type(texto)

    # Click em "avançar" depois do desafio de áudio
    click_mouse5()
    time.sleep(8)

@keyword
def retry_reCaptcha():
    
    # Biblioteca do sistema
    import os

    # Importação de time para utilização do Sleep
    import time

    # Bibliotecas para transcrição de áudio em texto e auxiliares
    # INSTALAR AS BIBLIOTECAS ABAIXO -> É NECESSÁRIO INSTALAR NA ORDEM ESPECIFICADA
    # 1. pip install NumPy
    # 2. pip install pipwin
    # 3. pipwin install pyaudio
    # 4. pip install pyautogui -> Para auxílio na utilização de Keys
    # 5. pip install google-api-python-client
    # 6. pip install monotonic -> Instalar apenas se o código der erro na transcrição do áudio.
    # 7. pip install speechrecognition -> Interpretador de fala
    # 8. pip install pynput

    # Transcrição de áudio em Texto
    import speech_recognition as sr

    # Conversção de metadados
    from speech_recognition import AudioData
    import os

    # Bibliotecas de linguagem
    import pyaudio

    # Biblioteca para gravação de frequências
    import wave

    # Biblioteca necessária para a utilização dos recursos de áudio (python)
    import pyautogui
    
    # Biblioteca de digitação (para digitar o texto do áudio no campo especificado).
    # pip install pynput
    import pynput
    from pynput.keyboard import Key, Controller

    # Importação de arquivo com as ações do mouse
    from support.mouse import click_mouse3, click_mouse4, click_mouse5

    # Exclui o arquivo de áudio do diretório, caso haja.
    try:
        os.remove('audio.wav')
        os.remove('texto.txt')
    except OSError:
        pass

    # GRAVAÇÃO DE AUDIO

    # Nome do arquivo de áudio com a terminação padrão "wav".
    arquivo_audio = 'audio.wav'
    
    # Clica no audio online para fazer a gravação
    click_mouse3()
    
    # **********
    # IMPORTANTE
    # **********

    # É necessário habilitar o "MIXAGEM ESTÉREO" como opção padrão de gravação em seu computador.
    # Para fazer isso, entre em "Alterar sons do sistema" -> Gravação -> Habilitar "Mixagem Estéreo" como dispositivo padrão (de preferência, desabilite os outros microfones).
    # É ncessário que a opção "Alto-falantes" em "REPRODUÇÃO" esteja habilitada com o volume de 60+ para que não hajam problemas de reconhecimento de fala.

    chunk = 2048                        # Define o tamanho de cada pedaço de áudio em 1024
    formato = pyaudio.paInt16           # Formata o arquivo em 16 bits
    canais = 2                          # Número de canais para o áudio
    fs = 44100                          # Grava em 44100 por segundo
    tempo = 6                           # Tempo de gravação
    
    p = pyaudio.PyAudio()               # Cria a porta de áudio Pyaudio

    # Abre uma gravação com os valores definidos acima:
    stream = p.open(format=formato,
                channels = canais,
                rate = fs,
                frames_per_buffer = chunk,
                input = True)
    frames = []

    # Faz a gravação em um arquivo
    for i in range(0, int(fs / chunk * tempo)):
        data = stream.read(chunk)
        frames.append(data)

    # Encerra a gravação
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Define os dados do arquivo WAV
    file = wave.open(arquivo_audio, 'wb')
    file.setnchannels(canais)
    file.setsampwidth(p.get_sample_size(formato))
    file.setframerate(fs)

    # Escreve e fecha o arquivo
    file.writeframes(b''.join(frames))
    file.close()
    time.sleep(2)

    # **************************************************************************
    # Finalização da gravação de áudio -> Início da tradução do áudio para texto
    # **************************************************************************

    # Cria um teclado para digitação sem necessidade de clicar em um elemento específico -> Biblioteca pynput:
    teclado = Controller()

    # Iniciação do Recognizer para transcriçaõ de áudio em texto
    r = sr.Recognizer()

    # Abertura do arquivo criado com o caminho absoluto(caminho diferente em outros computadores). 
    # Essencial deixar o caminho absoluto para não ocorrer erros ->> Coloque o caminho da pasta principal do projeto
    with sr.AudioFile('C:/Users/Luã Viana/Documents/Conteúdo para Repasse/POC - ROBOT/Portal - Robot/audio.wav') as source:

        # Definição de ártifices para redução de ruído
        r.energy_threshold = 400
        r.pause_threshold = 1.2
        r.dynamic_energy_threshold = True
        r.dynamic_energy_adjustment_damping = 0.30
        r.dynamic_energy_ratio = 1.5

        # Definição do áudio sem ruído e transcrição para texto com recognize_google.
        audio = r.record(source)
        texto = r.recognize_google(audio, language='en-US')

        # O áudio, por vezes, é arquivado em formato de lista. Para transformar em string é necessário fazer o passo abaixo:
        texto = ''.join(texto)

        # Caso o texto seja diferente de nulo e "alternativefinal"(mensagem de erro do recognize_google),
        # Ele irá anotar o texto em um bloco de notas para validação. Caso contrário, ele irá refazer o passo de tradução
        # Com um parametro chamado "Show_all=True", para mostrar o texto completo do arquivo sem necessidade de mostrar o erro anterior.
        if texto != "" or texto != "alternativefinal":

            # Abre um bloco de notas para digitação do texto:
            #->> Coloque o caminho da pasta principal do projeto
            with open('C:/Users/Luã Viana/Documents/Conteúdo para Repasse/POC - ROBOT/Portal - Robot/texto.txt', 'w+') as escrita:
                
                # Escreve o texto em um bloco de notas para validação
                escrita.write(texto)
                time.sleep(2)

                # Clica no campo de digitação do texto
                click_mouse4()
                time.sleep(2)

            # Digita o texto adquirido na tradução.    
            teclado.type(texto)
        else:
            #->> Coloque o caminho da pasta principal do projeto
            with sr.AudioFile('C:/Users/Luã Viana/Documents/Conteúdo para Repasse/POC - ROBOT/Portal - Robot/audio.wav') as source:
                
                # Definição de ártifices para redução de ruído
                r.energy_threshold = 400
                r.pause_threshold = 1.2
                r.dynamic_energy_threshold = True
                r.dynamic_energy_adjustment_damping = 0.30
                r.dynamic_energy_ratio = 1.5
                
                # Definição do áudio sem "noise" e transcrição para texto com recognize_google.
                # Diferença que este código em questão apresenta "Show_all=True", para mostrar todo o conteúdo traduzido.
                audio = r.record(source)
                texto = r.recognize_google(audio, language='en-US', show_all=True)

                # O áudio, por vezes, é arquivado em formato de lista. Para transformar em string é necessário fazer o passo abaixo:
                texto = ''.join(texto)

                # Abre um bloco de notas para digitação do texto:
                #->> Coloque o caminho da pasta principal do projeto
                with open('C:/Users/Luã Viana/Documents/Conteúdo para Repasse/POC - ROBOT/Portal - Robot/texto.txt', 'w+') as escrita:
                    
                    # Escreve o texto em um bloco de notas para validação
                    escrita.write(texto)
                    time.sleep(2)

                    # Clica no campo de digitação do texto
                    click_mouse4()
                    time.sleep(2)
                
                # Digita o texto adquirido na tradução
                teclado.type(texto)
    # Click em "avançar" depois do desafio de áudio
    click_mouse5()
    time.sleep(8)
    from robot.api import logger
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC

    class CustomLibrary:
        def __init__(self):
            self.driver = None
            self.driver.switch_to.default_content()