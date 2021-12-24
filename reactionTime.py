import time
from dotenv.main import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

config = dotenv_values(".env")

driver = webdriver.Chrome(config["CHROMEDRIVER_PATH"])

def play():

    driver.get("https://humanbenchmark.com/tests/reactiontime")
    time.sleep(1)

    div = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]')
    div.click()

    for i in range(0, 5):
        print("waiting")
        while "view-go" not in div.get_attribute("class"):
            pass
        print("green")

        div.click()
        time.sleep(1)
        div.click()

    save = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div[3]/button[1]')
    save.click()
    time.sleep(1)


driver.get("https://humanbenchmark.com")
time.sleep(1)

login = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/a[2]')
login.click()
time.sleep(1)

username = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/form/p[1]/input')
username.send_keys(config["USERNAME"])

password = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/form/p[2]/input')
password.send_keys(config["PASSWORD"])

login_submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div/div/form/p[3]/input')
login_submit.click()
time.sleep(1)

for i in range(0, 10):
    play()


