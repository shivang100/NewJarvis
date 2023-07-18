import os
import keyboard
import pyautogui
import webbrowser

from time import sleep

def openexe(querry):
    querry=str(querry).lower()

    if "launch" in querry:
        nameofweb=querry.replace("launch ","")
        link=f"https://www.{nameofweb}.com"
        webbrowser.open(link)
        return True
    
    elif "visit" in querry:
        nameofweb=querry.replace("visit ","")
        link=f"https://www.{nameofweb}.com"
        webbrowser.open(link)
        return True
        
    elif "open" in querry:
        nameofapp=querry.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameofapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True

    elif "start" in querry:
        nameofapp=querry.replace("start ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameofapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True

