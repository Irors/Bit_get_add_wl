import time
from random import choice
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def add_wl():
    alf = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

    options = Options()
    options.add_argument("start-maximized") # запуск браузера в полный экран
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    driver.get("https://www.bitget.com/login") #Переходим на сайт и логинимся
    WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div[3]/div/div[1]/ul/li[1]/a')))  # Ожидаем логин

    driver.get("https://www.bitget.com/asset/batchAdd?batchType=1") #Переходим по ссылке для добавления адресов
    WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div/div[3]/div/div[1]/div[3]/div/button')))  # Ожидаем

    input("\nНастройте какой токен вы хотите добавить и нажмите 'Enter' после всего\n")

    with open("address.txt") as file:
        addr = [i.strip() for i in file]

    for i in range(len(addr)-1):
        driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div/div[3]/div/div[1]/div[3]/div/button').click()  # кликаем на добавление адресов
        time.sleep(0.3)

    count = 1
    for wallet in addr:
        driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[3]/div/div[1]/div[3]/div/div[2]/div[{count}]/div[6]/div/input').send_keys(wallet)  # вводим адрес кошелька
        driver.find_element(By.XPATH, f'//*[@id="__layout"]/div/div/div[3]/div/div[1]/div[3]/div/div[2]/div[{count}]/div[8]/div/input').send_keys("".join([choice(alf) for i in range(10)]))  # вводим рандомное премечание

        time.sleep(0.1)
        count += 1

    input("\nГотово\n")
