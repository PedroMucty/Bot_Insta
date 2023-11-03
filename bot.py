from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicialize o WebDriver do Chrome
driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(5)

# Variáveis

campo_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
campo_senha = '//*[@id="loginForm"]/div/div[2]/div/label/input'
cancel_not = '_a9_1'
last_messages = 'N9d9h'

# Login
login = driver.find_element(By.XPATH, campo_login)
login.click()
login.send_keys('mano_rro')
time.sleep(0.5)

senha = driver.find_element(By.XPATH, campo_senha)
senha.click()
senha.send_keys('lolpkbr123')
time.sleep(0.5)

senha.send_keys(Keys.ENTER)
time.sleep(5)

# Lida com notificações (opcional)
try:
    noti = driver.find_element(By.CLASS_NAME, cancel_not)
    time.sleep(1)
    noti.click()
except Exception as e:
    print("Não foi possível lidar com notificações:", e)

# Navega até a página de mensagens
driver.get('https://www.instagram.com/direct/inbox/')

# Função para clicar nas últimas mensagens
def bot():
    try:
        last_messages = driver.find_element(By.CLASS_NAME,last_messages)
        last_messages = driver.find_elements(By.CLASS_NAME,last_messages)
        
        if last_messages[0].click():
            
            input()
    except Exception as e:
        print('Aguardando ou erro:')
        time.sleep(1)
        pass

while True:
    bot()