from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

def init():
    path = 'C://Users//yossi//Desktop//Python-Project//Trip_Yoetz_Automation_Project//Driver//chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get('https://trip-yoetz.herokuapp.com/login')
    driver.maximize_window()
    WebDriverWait(driver, 20)
    return driver

# -------------------------------------------------


# Login Objects:
EMAIL = "email"
PASSWORD = "password"
LOGIN_BUTTON = "login-btn"
ERROR_MESSAGE = "//div[2]/form[1]/h2[1]"
SHOW_PASSWORD = "visible-password-btn"

# Log In Correctly and Login Incorrectly:
def test_valid_email_valid_password():
    driver = init()
    # Send Value To The Email Field
    email = driver.find_element(By.NAME, EMAIL)
    email.send_keys("Yosef@gmail.com")
    # Send Value To The Password Field
    password = driver.find_element(By.NAME, PASSWORD)
    password.send_keys('123456')
    # Press On Login Button
    login_button = driver.find_element(By.CLASS_NAME, LOGIN_BUTTON)
    login_button.click()
    # Dismiss The Pop Out Alert
    WebDriverWait(driver, 5).until(EC.alert_is_present(), "Timed Out ")
    alert = driver.switch_to.alert
    alert.dismiss()
    # Forward The Driver One Page
    driver.forward()
    WebDriverWait(driver, 20)
# 2 Tests When Email is Valid:
def test_email_valid_password_invalid_and_null():
    value_error_message = 'password or email incorrect'
    email_value = 'Yosef@gmail.com'
    passwords = ['144444', '']
    driver = init()
    email = driver.find_element(By.NAME, EMAIL)
    password = driver.find_element(By.NAME, PASSWORD)
    login_button = driver.find_element(By.CLASS_NAME, LOGIN_BUTTON)
    for i in range(len(passwords)):
        # Start with Index 0 :
        email.send_keys(email_value)
        # Start with Index 0 :
        password.send_keys(passwords[i])
        # Press On Login Button :
        login_button.click()
        # Clear The Fields :
        email.clear(), password.clear()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, ERROR_MESSAGE)))
        # Print Message:
        error = driver.find_element(By.XPATH, ERROR_MESSAGE).get_attribute('innerText')
        assert error == value_error_message
# 3 Tests When Email is Invalid:
def test_invalid_email_password_valid_invalid_null():
    value_error_message = 'no user found'
    email_value = 'h123@gmail.com'
    passwords = ['147852', '1236666', '']
    driver = init()
    email = driver.find_element(By.NAME, EMAIL)
    password = driver.find_element(By.NAME, PASSWORD)
    login_button = driver.find_element(By.CLASS_NAME, LOGIN_BUTTON)
    for i in range(len(passwords)):
        email.send_keys(email_value)
        password.send_keys(passwords[i])
        login_button.click()
        email.clear(), password.clear()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, ERROR_MESSAGE)))
        error = driver.find_element(By.XPATH, ERROR_MESSAGE).text
        assert error == value_error_message
# 3 Tests When Email is Null:
def test_email_null_password_valid_invalid_null():
    driver = init()
    email_value = ''
    passwords = ['147852', '152452', '']
    value_error_message = 'no user found'
    email = driver.find_element(By.NAME, EMAIL)
    password = driver.find_element(By.NAME, PASSWORD)
    login_button = driver.find_element(By.CLASS_NAME, LOGIN_BUTTON)
    for i in range(len(passwords)):
        email.send_keys(email_value)
        password.send_keys(passwords[i])
        login_button.click()
        email.clear(), password.clear()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, ERROR_MESSAGE)))
        error = driver.find_element(By.XPATH, ERROR_MESSAGE).text
        assert error == value_error_message
# Show Password Button:
def test_show_password():
    driver = init()
    email = driver.find_element(By.NAME, EMAIL)
    password = driver.find_element(By.NAME, PASSWORD)
    show_password_button = driver.find_element(By.CLASS_NAME, SHOW_PASSWORD)
    login_button = driver.find_element(By.CLASS_NAME, LOGIN_BUTTON)
    email.send_keys('u8@gmail.com')
    password.send_keys('122')
    show_password_button.click()
    password.is_displayed()
    login_button.click()
# ------------------------------------------
# Top Links Objects:


TOP_LINKS = '//header/div/a'
# Links Test - Login, Register , About Us , Home-Page  :
def test__top_links():
    driver = init()
    top_links = driver.find_elements(By.XPATH, TOP_LINKS)
    for i in range(len(top_links)):
        if i != 0:
            top_links[i].click()
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, TOP_LINKS)))
            driver.back()
            WebDriverWait(driver, 20)

# -------------------------------------------
# Accessibility In One By One & One And Reset:


ACCESSIBILITY_BUTTON = "toggle-mode-btn"
ACCESSIBILITY_SECTION = '//div[2]/div[1]/button'
def test_accessibility_one_by_one():
    driver = init()
    button = driver.find_element(By.CLASS_NAME, ACCESSIBILITY_BUTTON)
    colors = driver.find_elements(By.XPATH, ACCESSIBILITY_SECTION)
    for i in range(len(colors)):
        WebDriverWait(driver, 30)
        button.click()
        driver.implicitly_wait(15)
        colors[i].click()

def test_accessibility_with_reset():
    driver = init()
    driver.implicitly_wait(15)
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
# -------------------------------------------
# Search Field:


SEARCH_FIELD = 'header-search-input'
ERROR_MESSAGE1 = "//h2[contains(text(),'no city found')]"
def test_search_correctly():
    driver = init()
    search_field = driver.find_element(By.CLASS_NAME, SEARCH_FIELD)

    # Search Correctly:
    search_field.send_keys('Paris')
    search_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 1).until(EC.url_to_be('https://trip-yoetz.herokuapp.com/cities'))

def test_search_incorrectly():
    driver = init()
    search_field = driver.find_element(By.CLASS_NAME, SEARCH_FIELD)
    search_field.send_keys('France')
    search_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 20)
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, ERROR_MESSAGE1)))

    error = driver.find_element(By.XPATH, ERROR_MESSAGE1).get_attribute('innerText')
    assert error == 'No City Found'

# ----------------------------------------------

# Navigate to Register Page:


REGISTER_LINK = "navigate-btn"
def test_register_link():
    driver = init()
    register_link = driver.find_element(By.CLASS_NAME, REGISTER_LINK)
    register_link.click()
    WebDriverWait(driver, 5).until(EC.url_to_be('https://trip-yoetz.herokuapp.com/register'))

# ------------------------------------------------
# Who Are We Section - Links


WHO_ARE_WE = 'open-footer-btn'
CONTACT_LINKS = "//article/div[1]/a"
PAGE_LINKS = '//footer[1]/div/a'
def test_who_are_we():
    driver = init()
    who_are_we_button = driver.find_element(By.CLASS_NAME, WHO_ARE_WE)
    contact_links = driver.find_elements(By.XPATH, CONTACT_LINKS)
    page_links = driver.find_elements(By.XPATH, PAGE_LINKS)
    who_are_we_button.click()
    driver.implicitly_wait(3)
    for i in range(len(page_links)):
        page_links[i].click()
        driver.implicitly_wait(3)
    for i in range(len(contact_links)):
        contact_links[i].click()

# ---------------------------------
# UI Test


TOP_SECTION = "header"
CENTER_SECTION = '#mainScroll'
BOTTOM_SECTION = '//footer[1]'
WHO_ARE_WE_DETAILS = '//div[1]/footer[1]'

def test_ui():
    driver = init()

    top_section = driver.find_element(By.CSS_SELECTOR, TOP_SECTION).text
    assert top_section == "Login\nRegister\nAbout us\nTripYoetz"

    center_section = driver.find_element(By.CSS_SELECTOR, CENTER_SECTION).text
    assert center_section == "New here ?\nTo register please click the link below\nRegister\nLogin\nLOGIN"

    who_are_we_button = driver.find_element(By.CLASS_NAME, WHO_ARE_WE)
    bottom_section = driver.find_element(By.XPATH, BOTTOM_SECTION).text
    assert bottom_section == "Who are we?"
    who_are_we_button.click()

    who_are_we_details = driver.find_element(By.XPATH, WHO_ARE_WE_DETAILS).get_attribute('innerText')
    assert who_are_we_details == "Marcos Bazbih\n24 years old, Ashdod\nTikva Yosef\n26 years old, Natanya\nAvi " \
                                 "Admaso\n26 years old, Ashdod\nWho are we?\nTripYoetz\nLearn more\ncopyright " \
                                 "?? | 2022 TripYoetz | all right reserved."
