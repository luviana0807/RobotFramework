*** Settings ***
Resource    producao.robot

*** Test Cases ***
Registro de login
    
    Dado que estou no site
    Quando acesso o campo de cadastro
    E realizo o cadastro
    Então a minha conta é criada
    Fim do fluxo