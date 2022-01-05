import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    for i in range(0, score-1):
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

    for i in range(0, 3):
        html = container.get_attribute('outerHTML')
        while "active" not in html:
            html = container.get_attribute('outerHTML')

        tile_htmls = html.split("eut2yre1")[:-1]
        flashed = ["active" in tile_html for tile_html in tile_htmls]

        time.sleep(1.5)

        tiles = container.find_elements(By.CLASS_NAME, "eut2yre1")
        for idx, tile in enumerate(tiles):
            if not flashed[idx]:
                tile.click()
            if len(container.find_elements(By.CLASS_NAME, "error")) == 3:
                break

        time.sleep(2)

    time.sleep(1)

    if loggedIn:
        save(driver)

def numberMemory(driver, loggedIn, score):

    driver.get("https://humanbenchmark.com/tests/number-memory")
    time.sleep(1)

    start = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button')
    start.click()

    for i in range(0, score-1):
        number = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[1]').text

        field = WebDriverWait(driver, 10 + i*2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[2]/input')))
        field.send_keys(number)

        submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[3]/button')
        submit.click()

        time.sleep(0.5)

        next = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button')
        next.click()

    field = WebDriverWait(driver, 10 + score*2).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[2]/input')))
    field.send_keys('L')

    submit = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/form/div[3]/button')
    submit.click()

    time.sleep(1)

    if loggedIn:
        save(driver)

def verbalMemory(driver, loggedIn, score):

    driver.get("https://humanbenchmark.com/tests/verbal-memory")
    time.sleep(1)

    start = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[4]/button')
    start.click()

    words = {}

    for i in range(0, score):
        word = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div').text

        if word in words:
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]').click()
        else:
            words[word] = 1
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]').click()

    for i in range(0, 3):
        word = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div').text

        if word in words:
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[2]').click()
        else:
            words[word] = 1
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[3]/button[1]').click()

    time.sleep(1)

    if loggedIn:
        save(driver)

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

def chimpTest(driver, loggedIn, score):

    driver.get("https://humanbenchmark.com/tests/chimp")
    time.sleep(1)

    start = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[2]/button')
    start.click()

    for i in range(0, score - 4):
        for j in range(1, i+5):
            driver.find_element(By.CSS_SELECTOR, f"[data-cellnumber='{j}']").click()

        cont = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[3]/button')
        cont.click()

    if score < 41:
        for i in range(0, 3):
            driver.find_element(By.CSS_SELECTOR, "[data-cellnumber='2']").click()

            if i < 2:
                cont = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[1]/div[3]/button')
                cont.click()

    time.sleep(1)

    if loggedIn:
        save(driver)

def sequenceMemory(driver, loggedIn, score):

    driver.get("https://humanbenchmark.com/tests/sequence")
    time.sleep(1)

    start = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/button')
    start.click()

    div = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div/div/div[2]/div')

    for i in range(0, score-1):
        tiles = {}

        for j in range(0, i+1):
            tile = WebDriverWait(div, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "active")))
            tiles[j] = tile
            time.sleep(0.5)

        for tile in tiles:
            tiles[tile].click()

    first = {}
    for i in range(0, score):
        if i == 0:
            first = WebDriverWait(div, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "active")))
        time.sleep(0.5)

    tiles = div.find_elements(By.CLASS_NAME, "square")
    for tile in tiles:
        if tile != first:
            tile.click()
            break

    time.sleep(1)

    if loggedIn:
        save(driver)
