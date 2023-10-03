*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

Resource   cod.robot

*** Variables ***
${url}=    https://automationexercise.com/


*** Keywords ***
Iniciar
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Title Should Be    Automation Exercise

Fim do fluxo
    Capture Page Screenshot
    Close All Browsers
