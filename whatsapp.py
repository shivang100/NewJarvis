from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
from selenium import webdriver
import pandas as pd
from Body.Speak import speak
import pathlib
from Body.Listen import MicExecution

scriptDirectory = pathlib.Path().absolute()

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
PathofDriver = "DataBase\\chromedriver.exe"
driver = webdriver.Chrome(PathofDriver,options=options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
speak("Initializing The Whatsapp Software.")

ListWeb = {'anubhav sir' : "9695382875",
            'me': "8936955375",
            "kshitij": '+917302341740'}

def whatsappsender(Name):
    speak(f"Preparing To Send a Message To {Name}")
    speak("What's The Message By The Way?")
    Message = MicExecution()
    Number = ListWeb[Name]
    LinkWeb = 'https://web.whatsapp.com/send?phone=' + Number + "&text=" + Message
    driver.get(LinkWeb)
    sleep(5)
    try:
        # driver.switch_to.window(driver.window_handles[0])
        driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        sleep(2)
        driver.find_element(by=By.XPATH,value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
        speak("Message Sent")
        
    except:
        print("Invalid Number")
# //*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span