import pyautogui

# 1 - Clicar e digitar meu usuario
pyautogui.click(681,383,duration=0.5)
pyautogui.write('john')

# 2 - Clicar e digitar minha senha
pyautogui.click(680,412,duration=0.5)
pyautogui.write('123456')

# 3 - Clicar em "entrar"
pyautogui.click(595,448,duration=0.5)

# 4 - Cadastrar os produtos
with open('produtos.txt','r') as arquivo:
  for linha in arquivo:
    produto = linha.split(',')[0]
    quantidade = linha.split(',')[1]
    preco = linha.split(',')[2]

    # 1 - Clicar e digitar o produto
    pyautogui.click(399,376,duration=0.5)
    pyautogui.write(produto)

    # 2 - Clicar e digitar a quantidade
    pyautogui.click(399,397,duration=0.5)
    pyautogui.write(quantidade)

    # 3 - Clicar e digitar o preço
    pyautogui.click(397,426,duration=0.5)
    pyautogui.write(preco)

    # 4 - Clicar em "Cadastrar"
    pyautogui.click(318,580,duration=0.5)