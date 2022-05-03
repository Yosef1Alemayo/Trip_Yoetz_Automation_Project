from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

# Login Objects:
EMAIL = "email"
PASSWORD = "password"
LOGIN_BUTTON = "login-btn"

def init():
    path = 'C://Users//yossi//Desktop//Python-Project//Trip_Yoetz_Automation_Project//Driver//chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get('https://trip-yoetz.herokuapp.com/login')
    driver.maximize_window()
    email = driver.find_element(By.NAME, EMAIL)
    email.send_keys("Yosef@gmail.com")
    password = driver.find_element(By.NAME, PASSWORD)
    password.send_keys('123456')
    login_button = driver.find_element(By.CLASS_NAME, LOGIN_BUTTON)
    login_button.click()
    WebDriverWait(driver, 5).until(EC.alert_is_present(), "Timed Out ")
    alert = driver.switch_to.alert
    alert.accept()
    driver.refresh()
    return driver

# --------------------------------------------
# Log Out Correctly After Connection:


LOG_OUT_BUTTON = '//header[1]/div[1]/button[1]'
def test_log_out_correctly():
    driver = init()
    WebDriverWait(driver, 20)
    log_out_button = driver.find_element(By.XPATH, LOG_OUT_BUTTON)
    log_out_button.click()
    driver.implicitly_wait(5)
    alert = driver.switch_to.alert
    alert.accept()
    alert.accept()
    WebDriverWait(driver, 20)

# --------------------------------------------

# Navigate To Top Links:


TOP_LINKS = "//header/div/a"
def test_links():
    driver = init()
    top_links = driver.find_elements(By.XPATH, TOP_LINKS)
    for i in range(len(top_links)):
        if i != 0:
            top_links[i].click()
            WebDriverWait(driver, 20)
            driver.back()
            WebDriverWait(driver, 15)

# --------------------------------------------
# Who Are We Section: Links


WHO_ARE_WE = '//footer[1]/button[1]'
CONTACT_LINKS = "//article/div[1]/a"
PAGE_LINKS = '//footer[1]/div/a'
def test_who_are_we():
    driver = init()
    who_are_we_button = driver.find_element(By.XPATH, WHO_ARE_WE)
    driver.implicitly_wait(15)
    who_are_we_button.click()
    WebDriverWait(driver, 20)
    page_links = driver.find_elements(By.XPATH, PAGE_LINKS)
    for i in range(len(page_links)):
        page_links[i].click()
        driver.implicitly_wait(15)
    contact_links = driver.find_elements(By.XPATH, CONTACT_LINKS)
    for i in range(len(contact_links)):
        contact_links[i].click()
        driver.implicitly_wait(15)

# --------------------------------------------

# Accessibility:


ACCESSIBILITY_BUTTON = "toggle-mode-btn"
ACCESSIBILITY_SECTION = '//div[2]/div[1]/button'
def test_accessibility_one_by_one():
    driver = init()
    button = driver.find_element(By.CLASS_NAME, ACCESSIBILITY_BUTTON)
    colors = driver.find_elements(By.XPATH, ACCESSIBILITY_SECTION)
    for i in range(len(colors)):
        driver.implicitly_wait(15)
        WebDriverWait(driver, 20)
        button.click()
        driver.implicitly_wait(15)
        colors[i].click()

def test_accessibility_with_reset():
    driver = init()
    button = driver.find_element(By.CLASS_NAME, ACCESSIBILITY_BUTTON)
    colors = driver.find_elements(By.XPATH, ACCESSIBILITY_SECTION)
    for i in range(len(colors)):
        driver.implicitly_wait(15)
        button.click()
        driver.implicitly_wait(15)
        colors[i].click()
        if i == 0:
            continue
        button.click()
        driver.implicitly_wait(15)
        colors[0].click()
# --------------------------------------------
# Search Field :


SEARCH_FIELD = '//form[1]/input[1]'
ERROR_MESSAGE = "//h2[contains(text(),'no city found')]"
def test_search_correctly():
    driver = init()
    search_field = driver.find_element(By.XPATH, SEARCH_FIELD)
    WebDriverWait(driver, 20)
    search_field.send_keys('Paris')
    search_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.url_to_be('https://trip-yoetz.herokuapp.com/cities'))

def test_search_incorrectly():
    driver = init()
    search_field = driver.find_element(By.XPATH, SEARCH_FIELD)
    driver.implicitly_wait(15)
    search_field.send_keys('France')
    search_field.send_keys(Keys.ENTER)
    driver.implicitly_wait(15)
    error = driver.find_element(By.XPATH, ERROR_MESSAGE).get_attribute('innerText')
    assert error == 'No City Found'

# --------------------------------------------
# Edit Profile Correctly and Incorrectly :
# Bug in The Edit Profile Incorrectly:


EDIT_BUTTON = '//div[1]/div[1]/button[1]'
UPDATE_SECTION = '//section[1]/div[3]/form[1]/input'
UPDATE_BUTTON = '//form[1]/button[1]'
def test_edit_profile_correctly():
    driver = init()
    WebDriverWait(driver, 20)
    edit_button = driver.find_element(By.XPATH, EDIT_BUTTON)
    edit_button.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, EDIT_BUTTON)))

    update_section = driver.find_elements(By.XPATH, UPDATE_SECTION)

    update_button = driver.find_element(By.XPATH, UPDATE_BUTTON)

    values = ['Natan', 'Elias', 'Yosef@gmail.com', '26/11/1996', 'Spain.png']

    for i in range(len(values)):
        update_section[i].clear()
        update_section[i].send_keys(values[i])
        WebDriverWait(driver, 20)
    update_button.click()
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    WebDriverWait(driver, 20)

    for i in range(len(values)):
        update_section[i].clear()
        if i != 0:
            update_section[i].send_keys(values[i])
            WebDriverWait(driver, 20)
    update_button.click()
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    for i in range(len(values)):
        update_section[i].clear()
        if i != 1:
            update_section[i].send_keys(values[i])
            WebDriverWait(driver, 20)
    update_button.click()
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

    for i in range(len(update_section)):
        update_section[i].clear()
        if i != 4:
            update_section[i].send_keys(values[i])
            WebDriverWait(driver, 20)
    update_button.click()
    WebDriverWait(driver, 20).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()

def test_edit_profile_incorrectly():
    driver = init()
    WebDriverWait(driver, 20)
    edit_button = driver.find_element(By.XPATH, EDIT_BUTTON)
    edit_button.click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, EDIT_BUTTON)))

    update_section = driver.find_elements(By.XPATH, UPDATE_SECTION)

    update_button = driver.find_element(By.XPATH, UPDATE_BUTTON)

    values1 = ['-', '-', '123', '', '.-']

    for i in range(len(values1)):
        update_section[i].clear()
        update_section[i].send_keys(values1[i])
    update_button.click()

    WebDriverWait(driver, 20)

    values2 = ['Yosef', 'Alemayo', '123', '26/11/1988', 'k.png']

    for i in range(len(values2)):
        update_section[i].clear()
        update_section[i].send_keys(values2[i])
    update_button.click()

    WebDriverWait(driver, 20)

    values3 = ['Yosef', 'Alemayo', 'Yosef@gmail.com', '-----', 'k.png']

    for i in range(len(values3)):
        update_section[i].clear()
        update_section[i].send_keys(values3[i])
    update_button.click()

    WebDriverWait(driver, 20)
# ------------------------------------------
# UI Test:


TOP_SECTION = 'header'
CENTER_SECTION = '//section[1]/section[1]/section[1]'
BOTTOM_SECTION = '//footer[1]/button[1]'
WHO_ARE_WE_DETAILS = '//div[1]/footer[1]'

def test_ui():
    driver = init()
    top_section = driver.find_element(By.CSS_SELECTOR, TOP_SECTION).get_attribute('innerText')
    assert top_section == "About us\nTripYoetz"

    center_section = driver.find_element(By.XPATH, CENTER_SECTION).get_attribute('innerText')
    assert center_section == "YOUR INFORMATION\nName: Yosef Alemayo\nAge: 34\nEmail: Yosef@gmail.com\nA member" \
                             " since: 2022-05-01\nYOUR FAVORITES\nNo favorites yet"

    bottom_section = driver.find_element(By.XPATH, BOTTOM_SECTION).get_attribute('innerText')
    assert bottom_section == "Who are we?"

    who_we_are = driver.find_element(By.XPATH, WHO_ARE_WE)
    who_we_are.click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, WHO_ARE_WE_DETAILS)))

    who_are_we_details = driver.find_element(By.XPATH, WHO_ARE_WE_DETAILS).get_attribute('innerText')
    assert who_are_we_details == "Marcos Bazbih\n24 years old, Ashdod\nTikva Yosef\n26 years old, Natanya\nAvi " \
                                 "Admaso\n26 years old, Ashdod\nWho are we?\nTripYoetz\nLearn more\ncopyright " \
                                 "© | 2022 TripYoetz | all right reserved."
