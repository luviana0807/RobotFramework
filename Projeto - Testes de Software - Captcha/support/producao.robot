*** Settings ***
Library     SeleniumLibrary
Library     Collections
Library     OperatingSystem

*** Variables ***
${url}      https://patrickhlauke.github.io/recaptcha/


*** Keywords ***
Iniciar
    Open Browser                    ${url}       Chrome
    Maximize Browser Window
    Title Should Be    Google reCAPTCHA test

Fechar
    Capture Page Screenshot
    Close Browser