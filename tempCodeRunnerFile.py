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