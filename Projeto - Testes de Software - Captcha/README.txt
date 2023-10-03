Realizando o desafio do Captcha usando Python + Robot + Selenium! 🤖🖥️

Fala pessoal, fiz esse teste para realizar em alguns cenários que estão no ambiente de produção e que não possuem possibilidade de serem testados em outros ambientes (sabemos que nem todos possuem uma infra muito robusta para fazer testes em DEV/HML/TST).

Dessa forma, realizei um pequeno cenário onde é possível automatizar o desafio do Captcha usando a opção para surdos com speechrecognition e outras ferramentas.

O que o código faz? Em resumo, o código faz os clicks através de uma biblioteca de controle do mouse, capta o áudio com uma biblioteca de transcrição de idiomas, salva o arquivo de áudio e depois converte o mesmo em texto. Após isso, o sistema pega o texto e coloca no campo desejado para realizar o desafio do captcha. Lembrando que, para que o computador grave o áudio do seu próprio sistema e não do seu microfone, troque o dispositivo de gravação para o "Mixagem Estéreo", pois ele deixa você gravar os sons do seu sistema.

A integração do python com o robot é através de uma biblioteca do próprio robot capaz de converter as classes em keywords. Era possível fazer apenas no python? Sim, é totalmente possível, mas quis mesclar python + robot hahahahaha.

É importante ressaltar que este tipo de teste não pode ser usado com muita frequência por conta do sistema de segurança do google responsável pelo Captcha ser monitorado, então hora ou outra percebem que é um robô fazendo essas requisições. Caso se interessem em automatizar este tipo de cenário, sugiro que façam essa automação com um espaço de, pelo menos uns 40min+.

Bibliotecas utilizadas:

    # 1. pip install NumPy
    # 2. pip install pipwin
    # 3. pipwin install pyaudio
    # 4. pip install pyautogui -> Para auxílio na utilização de Keys
    # 5. pip install google-api-python-client
    # 6. pip install monotonic -> Instalar apenas se o código der erro na transcrição do áudio.
    # 7. pip install speechrecognition -> Interpretador de fala
    # 8. pip install pynput