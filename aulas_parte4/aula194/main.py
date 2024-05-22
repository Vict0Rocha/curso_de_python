from pathlib import Path
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.chrome.service import Service

# ROOT_FOLDER = Path(__file__).parent
# CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drive' / 'chrome-headless-shell.exe' 

 # Configurações que vamos passar
chrome_options = webdriver.ChromeOptions()
 # O navegador em si
chrome_browser = webdriver.Chrome(
    options=chrome_options,
)

TIME_TO_WAIT = 10
# Abrindo o navegador
chrome_browser.get('https://www.google.com.br/?hl=pt-BR')

# Esperando o elemento aparecer na tela
search_input = WebDriverWait(chrome_browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, 'gLFyf')
    )
)
search_input.send_keys('Hello, World')
search_input.send_keys(Keys.ENTER)
sleep(TIME_TO_WAIT)