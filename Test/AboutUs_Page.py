from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def init():
    path = 'C://Users//yossi//Desktop//pythonProject//Driver//chromedriver.exe'
    driver = webdriver.Chrome(path)
    driver.get('https://trip-yoetz.herokuapp.com/about')
    driver.maximize_window()
    WebDriverWait(driver, 20)
    return driver


# --------------------------
TOP_LINKS = "//header/div/a"
def test_links():
    driver = init()
    top_links = driver.find_elements(By.XPATH, TOP_LINKS)
    for i in range(len(top_links)):
        if i != 2:
            top_links[i].click()
            sleep(3)
            WebDriverWait(driver, 20)
            driver.back()
            sleep(3)


# --------------------------
WHO_ARE_WE = '//footer[1]/button[1]'
CONTACT_LINKS = "//article/div[1]/a"
PAGE_LINKS = '//footer[1]/div/a'
def test_who_are_we():
    driver = init()
    who_are_we_button = driver.find_element(By.XPATH, WHO_ARE_WE)
    driver.implicitly_wait(15)
    who_are_we_button.click()
    sleep(3)
    page_links = driver.find_elements(By.XPATH, PAGE_LINKS)
    for i in range(len(page_links)):
        page_links[i].click()
        driver.implicitly_wait(15)
        sleep(2)
    contact_links = driver.find_elements(By.XPATH, CONTACT_LINKS)
    for i in range(len(contact_links)):
        contact_links[i].click()
        driver.implicitly_wait(15)
        sleep(2)


# --------------------------
SEARCH_FIELD = '//form[1]/input[1]'
ERROR_MESSAGE = '//h2'
def test_search_correctly():
    driver = init()
    search_field = driver.find_element(By.XPATH, SEARCH_FIELD)
    sleep(2)
    search_field.send_keys('Paris')
    search_field.send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.url_to_be('https://trip-yoetz.herokuapp.com/cities'))

# Need To Fix:
def test_search_incorrectly():
    driver = init()
    search_field = driver.find_element(By.XPATH, SEARCH_FIELD)
    driver.implicitly_wait(15)
    search_field.send_keys('France')
    search_field.send_keys(Keys.ENTER)
    driver.implicitly_wait(15)
    error = driver.find_element(By.XPATH, ERROR_MESSAGE).get_attribute('outerHTML')
    assert error == "<h2 class=\"error-msg\">no city found</h2>"


# --------------------------
# Can't find The Map Link and The Text:
MAP_LINK = '//body[1]/div[1]/div[1]/section[1]/section[1]/div[3]/iframe'
def test_map_link():
    driver = init()
    map_link = driver.find_element(By.XPATH, MAP_LINK)
    print(map_link.get_attribute('innerText'))


# Accessibility Test:
ACCESSIBILITY_BUTTON = "toggle-mode-btn"
ACCESSIBILITY_SECTION = '//div[2]/div[1]/button'
def test_accessibility_one_by_one():
    driver = init()
    button = driver.find_element(By.CLASS_NAME, ACCESSIBILITY_BUTTON)
    colors = driver.find_elements(By.XPATH, ACCESSIBILITY_SECTION)
    for i in range(len(colors)):
        WebDriverWait(driver, 20)
        button.click()
        driver.implicitly_wait(15)
        colors[i].click()

def test_accessibility_with_reset():
    driver = init()
    button = driver.find_element(By.CLASS_NAME, ACCESSIBILITY_BUTTON)
    colors = driver.find_elements(By.XPATH, ACCESSIBILITY_SECTION)
    for i in range(len(colors)):
        button.click()
        sleep(2)
        colors[i].click()
        sleep(3)
        if i == 0:
            continue
        button.click()
        sleep(3)
        colors[0].click()


# UI Test:
TOP_SECTION = 'header'
CENTER_SECTION = '//section[1]/section[1]'
BOTTOM_SECTION = '//footer[1]/button[1]'
WHO_ARE_WE_DETAILS = '//article'
COPY_RIGHTS_AND_LINKS = '//footer[1]/div[1]'
def test_ui():
    driver = init()
    top_section = driver.find_element(By.CSS_SELECTOR, TOP_SECTION).get_attribute('innerText')
    assert top_section == "Login\nRegister\nAbout us\nTripYoetz"

    center_section = driver.find_element(By.XPATH, CENTER_SECTION).get_attribute('innerText')
    assert center_section == "welcome to tripYoetz\nAbout Us\nTripYoetz, the world's largest travel guidance" \
                             " platform, helps hundreds of millions of people each month become better travelers," \
                             " from planning to booking to taking a trip. Travelers across the globe use the" \
                             " Tripadvisor site and app to discover where to stay, what to do and where to eat " \
                             "based on guidance from those who have been there before. With more than 1 billion " \
                             "reviews and opinions of nearly 8 million businesses, travelers turn to Tripadvisor to " \
                             "find deals on accommodations, book experiences, reserve tables at delicious restaurants" \
                             " and discover great places nearby. As a travel guidance company available in 43 markets" \
                             " and 22 languages, Tripadvisor makes planning easy no matter the trip type.\nContact" \
                             " Us\n\n054-8789426\n\ncontact@TripYoetz.com\n\n24 / 7\n\nMeet the team\nMarcos" \
                             " Bazbih\n24 years old, Ashdod\nFull Stack Developer\nTikva Yosef\n26 years old," \
                             " Natanya\nFull Stack Developer\nAvi Admaso\n26 years old, Ashdod\nFull Stack " \
                             "Developer\nFollow the links below for more info"

    bottom_section = driver.find_element(By.XPATH, BOTTOM_SECTION).get_attribute('innerText')
    assert bottom_section == "Who are we?"

    who_we_are = driver.find_element(By.XPATH, WHO_ARE_WE)
    who_we_are.click()
    sleep(5)

    contacts_details = driver.find_elements(By.XPATH, WHO_ARE_WE_DETAILS)
    details = ["Marcos Bazbih\n24 years old, Ashdod", "Tiva Yosef\n26 years"
               " old, Natanya", "Avi Amaso\n26 years old, Ashdod"]
    for i in range(len(contacts_details)):
        x = contacts_details[i].get_attribute('innerText')
        if x == details[0] or x == details[1] or x == details[2]:
            print('\n UI is Passed')
        else:
            print('\n UI is Failed')

    copy_rights_and_links = driver.find_element(By.XPATH, COPY_RIGHTS_AND_LINKS).get_attribute('innerText')
    assert copy_rights_and_links == "TripYoetz\nLearn more\ncopyright © | 2022 TripYoetz | all right reserved."
