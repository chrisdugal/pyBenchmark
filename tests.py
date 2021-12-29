import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def save(driver):
    save = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div[3]/button[1]')
    save.click()
    time.sleep(1)

def reactionTime(driver, loggedIn):

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

    if loggedIn:
        save(driver)

# TODO
def visualMemory(driver, loggedIn, score):
    pass

# TODO
def numberMemory(driver, loggedIn, score):
    pass

# TODO
def verbalMemory(driver, loggedIn, score):
    pass

def typing(driver, loggedIn):

    driver.get("https://humanbenchmark.com/tests/typing")
    time.sleep(1)

    div = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[2]/div')
    children = div.find_elements(By.TAG_NAME, "span")

    text = ""
    for child in children:
        text += child.text
        if child.text == "":
            text += " "

    div.send_keys(text)

    if loggedIn:
        save(driver)

# TODO
def aimTrainer(driver, loggedIn):
    pass

# TODO
def chimpTest(driver, loggedIn, score):
    pass

# TODO
def sequencyMemory(driver, loggedIn, score):
    pass
