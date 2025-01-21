# passo 1 : entrar no sitema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui

import pyautogui
import time
# pyautogui.write -> escreve um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> aperta um atalho (ctrl c)

pyautogui.PAUSE = 1.80

# abrir o navegador
# apertar a tecla win

pyautogui.press("win")
pyautogui.write("Microsoft edge")
pyautogui.press("enter")



# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(1)
pyautogui.press("enter")
# uma pausa de 3 segundos

time.sleep(1) 
pyautogui.click(x=445, y=362)

# passo 2 : fazer login

pyautogui.write("juanmuitocorno@gmail.com")
pyautogui.press("tab")
pyautogui.write("minhasenha")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# passo 3 : importar base de dados

import pandas

tabelas = pandas.read_csv("produtos(1).csv")
print(tabelas)