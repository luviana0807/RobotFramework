*** Settings ***
# Resource é uma forma de implementar o código de outro arquivo robot para o projeto.
Resource        ../support/producao.robot

# Library é uma forma de buscar uma biblioteca especifica ou um outro arquivo python.
Library         init_recaptcha.py


*** Test Cases ***
Teste_ReCaptcha
    Iniciar
    Re Captcha
    Sleep    5

##################################################################################################################################

# Importante falar que o teste não vai ser executado conforme esperado caso seu chromedriver esteja desatualizado e as ferramentas
# não forem estaladas conforme especificado. As bibliotecas a serem instaladas estão no arquivo "init_recaptcha.py"

##################################################################################################################################