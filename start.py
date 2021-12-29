import time
from dotenv.main import dotenv_values
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import tests

config = dotenv_values(".env")

driver = webdriver.Chrome(config["CHROMEDRIVER_PATH"])

driver.get("https://humanbenchmark.com")
time.sleep(1)

loggedIn = False

try:
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

    loggedIn = True

except:
    print("login failed")


for i in range(0, int(config["REACTION_TIME_ROUNDS"])):
    tests.reactionTime(driver, loggedIn)

for i in range(0, int(config["VISUAL_MEMORY_ROUNDS"])):
    tests.visualMemory(driver, loggedIn, int(config["VISUAL_MEMORY_SCORE"]))

for i in range(0, int(config["NUMBER_MEMORY_ROUNDS"])):
    tests.numberMemory(driver, loggedIn, int(config["NUMBER_MEMORY_SCORE"]))

for i in range(0, int(config["VERBAL_MEMORY_ROUNDS"])):
    tests.verbalMemory(driver, loggedIn, int(config["VERBAL_MEMORY_SCORE"]))

for i in range(0, int(config["TYPING_ROUNDS"])):
    tests.typing(driver, loggedIn)

for i in range(0, int(config["AIM_TRAINER_ROUNDS"])):
    tests.aimTrainer(driver, loggedIn)

for i in range(0, int(config["CHIMP_TEST_ROUNDS"])):
    tests.chimpTest(driver, loggedIn, int(config["CHIMP_TEST_SCORE"]))

for i in range(0, int(config["SEQUENCE_MEMORY_ROUNDS"])):
    tests.sequencyMemory(driver, loggedIn, int(config["SEQUENCE_MEMORY_SCORE"]))

