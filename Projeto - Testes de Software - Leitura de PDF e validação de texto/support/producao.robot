*** Settings ***
Library     SeleniumLibrary
Library     Collections
Library     OperatingSystem
Library     String

*** Variables ***
${url}      https://google.com


*** Keywords ***
Iniciar
    Open Browser                    ${url}       Chrome
    Maximize Browser Window

Fechar
    Capture Page Screenshot
    Close Browser