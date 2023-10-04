from PyPDF2 import PdfReader
import re
import os
from robot.api.deco import keyword

@keyword
def lerPdf(caminhopdf):

    caminhopdf = open(caminhopdf, 'rb')
    ler_pdf = PdfReader(caminhopdf)
    page = ler_pdf.pages[0]
    page_cont = page.extract_text()
    junct = ''.join(page_cont)
    junct = re.sub('n', '', junct)

    try:
        os.remove('lerpdf.txt')
    except OSError:
        pass

    with open('lerpdf.txt', 'w', encoding='utf-8') as leiturapdf:
        leiturapdf.write(junct)