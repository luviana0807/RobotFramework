*** Settings ***
# Resource é uma forma de implementar o código de outro arquivo robot para o projeto.
Resource        ../support/producao.robot

# Library é uma forma de buscar uma biblioteca especifica ou um outro arquivo python.
Library         ler_pdf.py

*** Variables ***
# Alterar caminho onde seu pdf está
${caminhoPDF}=       C:/QAx/RobotFramework/pdfdeteste.pdf
${arquivoTXT}=       lerpdf.txt
${cont_esperado}=    Robot Framework

*** Test Cases ***
Leitura de PDF
    Ler Pdf    ${caminhoPDF}
    ${conteudo_do_arquivo}=    Get File    ${arquivoTXT}
    Should Contain    ${conteudo_do_arquivo}    ${cont_esperado}