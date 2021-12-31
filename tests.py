import time
from selenium.webdriver.common.by import By

def save(driver):

    save = driver.find_element(By.CLASS_NAME, 'e19owgy710')
    save.click()
    time.sleep(1)

def reactionTime(driver, loggedIn):

    driver.get("https://humanbenchmark.com/tests/reactiontime")
    time.sleep(1)

    div = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]')
    div.click()

    for i in range(0, 5):
        while "view-go" not in div.get_attribute("class"):
            pass

        div.click()
        time.sleep(1)
        div.click()

    time.sleep(1)

    if loggedIn:
        save(driver)

def visualMemory(driver, loggedIn, score):

    driver.get("https://humanbenchmark.com/tests/memory")
    time.sleep(1)

    start = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button')
    start.click()

    container = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div')

    for i in range(0, score):
        html = container.get_attribute('outerHTML')
        while "active" not in html:
            html = container.get_attribute('outerHTML')

        tile_htmls = html.split("eut2yre1")[:-1]
        flashed = ["active" in tile_html for tile_html in tile_htmls]

        time.sleep(1.5)

        tiles = container.find_elements(By.CLASS_NAME, "eut2yre1")
        for idx, tile in enumerate(tiles):
            if flashed[idx]:
                tile.click()

        time.sleep(1)

    losses = 0
    while losses < 3:
        time.sleep(3)
        tiles = container.find_elements(By.CLASS_NAME, "eut2yre1")
        for tile in tiles:
            tile.click()
            if len(container.find_elements(By.CLASS_NAME, "error")) == 3:
                losses += 1
                break

    time.sleep(1)

    if loggedIn:
        save(driver)

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

    time.sleep(1)

    if loggedIn:
        save(driver)

def aimTrainer(driver, loggedIn):

    driver.get("https://humanbenchmark.com/tests/aim")
    time.sleep(1)

    div = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]')

    for i in range(0, 31):
        target = div.find_elements(By.CLASS_NAME, "e6yfngs4")[1]
        target.click()

    time.sleep(1)

    if loggedIn:
        save(driver)

# TODO
def chimpTest(driver, loggedIn, score):
    pass

# TODO
def sequenceMemory(driver, loggedIn, score):
    pass
