##################################################################################################################################

# Para conseguir saber a localização do seu mouse em tela abra o CMD e instancie o python com os comandos acima.
# Depois de importar e digitar 'mouse.position', as direções do seu mouse são mostradas no CMD, aí basta alterar para as dimensões do seu pc.
# As dimensões que utilizei são para um computador de 15 polegadas.

##################################################################################################################################

# pip install pynput - para controle do mouse e teclado

from robot.api.deco import keyword
from selenium.webdriver.chrome import options

@keyword
def click_mouse1():
    # Clica no reCaptcha
    import pynput
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (41, 317) # Valores relativos, auterar de acordo com o PC.
    return mouse.click(Button.left, 1)

@keyword
def click_mouse2():
    # Clica no desafio de áudio
    import pynput
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (149, 840) # Valores relativos, auterar de acordo com o PC.

    return mouse.click(Button.left, 1)

@keyword
def click_mouse3():
    # Clica na reprodução de áudio
    import pynput
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (218, 243) # Valores relativos, auterar de acordo com o PC.

    return mouse.click(Button.left, 1)

@keyword
def click_mouse4():
    # Clica no Input do captcha para colocar o texto
    import pynput
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (281, 355) # Valores relativos, auterar de acordo com o PC.
    mouse.click(Button.left, 1)

@keyword
def click_mouse5():
    # Clica em "VERIFICAR" depois de escrever no input do capcha
    import pynput
    from pynput.mouse import Button, Controller
    mouse = Controller()
    mouse.position = (314, 475) # Valores relativos, auterar de acordo com o PC.

    return mouse.click(Button.left, 1)


##################################################################################################################################

# Para conseguir saber a localização do seu mouse em tela abra o CMD e instancie o python com os comandos acima.
# Depois de importar e digitar 'mouse.position', as direções do seu mouse são mostradas no CMD, aí basta alterar para as dimensões do seu pc.
# As dimensões que utilizei são para um computador de 15 polegadas.

##################################################################################################################################