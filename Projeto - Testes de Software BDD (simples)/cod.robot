*** Settings ***
Resource    producao.robot

*** Keywords ***
Dado que estou no site
    Iniciar

Quando acesso o campo de cadastro
    Wait Until Element Is Enabled    //a[@href="/login"]
    Click Element    //a[@href="/login"]
    Title Should Be    Automation Exercise - Signup / Login

E realizo o cadastro
    # Inserção de nome
    Wait Until Element Is Enabled    //input[@placeholder="Name"]
    Input Text    //input[@placeholder="Name"]    seuNomedeTeste
    
    # Inserção de e-mail
    Wait Until Element Is Enabled    //input[@data-qa="signup-email"]
    Input Text    //input[@data-qa="signup-email"]    testedeemailrobotframework@g.com

    # Clicar no botão
    Click Button    Signup

    # Continuação do cadastro
    Title Should Be    Automation Exercise - Signup
    Select Radio Button    title    id_gender1
    
    # Senha
    Input Text    password    123
    
    # Datas
    Select From List By Value    //select[@id="days"]    2
    
    Select From List By Value    //select[@id="months"]    3

    Select From List By Value    //select[@id="years"]    1998

    # Informações de Endereço
    Input Text    first_name    Luã
    Input Text    last_name     Viana
    Input Text    company       Compania de Teste

    Input Text    address1      teste de endereço

    Select From List By Value    //select[@id="country"]    Canada

    Input Text    state         estado de teste
    Input Text    city          cidade de teste
    Input Text    zipcode       71000381
    Input Text    mobile_number    (61) 9 9999-9999

    Sleep    5
    Click Button    Create Account

Então a minha conta é criada
    Title Should Be    Automation Exercise - Account Created