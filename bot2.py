from selenium import webdriver
import time
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(5)


##driver.find_element(By.XPATH,VARIAVEL)
##driver.find_element(By.CLASS_NAME,VARIAVEL)
##driver.find_element(By.TAG_NAME,VARIAVEL)

#VARIAVEIS
campo_login = '//*[@id="loginForm"]/div/div[1]/div/label/input'
campo_senha = '//*[@id="loginForm"]/div/div[2]/div/label/input'
cancel_not = '_a9_1'
noti_mensagem = 'N9d9h'
#Login

login = driver.find_element(By.XPATH,campo_login)
login.click()
login.send_keys('mano_rro')
time.sleep(0.5)
senha = driver.find_element(By.XPATH,campo_senha)
senha.click()
senha.send_keys('lolpkbr123')
time.sleep(0.5)
senha.send_keys(Keys.ENTER)
time.sleep(5)
noti = driver.find_element(By.CLASS_NAME,cancel_not)
time.sleep(1)
noti.click()
time.sleep(5)
driver.get('https://www.instagram.com/direct/inbox/')

def bot():
    try:
       #clicar na nova mensagem
       bolinha = driver.find_element_by_class_name(noti_mensagem)
       bolinha = driver.find_elements_by_class_name(noti_mensagem)
       clica_last_mens = bolinha[0]
       acao_notifo = webdriver.common.action_chains.ActionChains(driver)
       acao_notifo.move_to_element_with_offset(clica_last_mens,0,-20)
       acao_notifo.click()
       acao_notifo.perform()

    except:
        print('aguarde')
        time.sleep(1)

while True:
    bot()