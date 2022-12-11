import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

opcoes = Options()
#opções.add_argument('--headless')
navegador = Chrome(service=Service(ChromeDriverManager().install()), options=opcoes)
navegador.set_window_size(1200, 1080)
navegador.maximize_window()

navegador.get('http://127.0.0.1:8000')
navegador.save_screenshot('raspagem.png')
navegador.close()