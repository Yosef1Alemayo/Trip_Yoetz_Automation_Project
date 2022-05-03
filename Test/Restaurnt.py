from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def int():
    driver = webdriver.Chrome("C://Users//yossi//Desktop//Trip_Yoetz_Automation_Project//Driver//chromedriver.exe")
    driver.get("https://trip-yoetz.herokuapp.com/login")
    driver.maximize_window()
    return driver

def test_login():
    driver = int()
    driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/section[1]/section[1]/div[2]/form[1]/div[1]/input[1]").send_keys("gonathan46@gmail.com")
    sleep(2)
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/section[1]/section[1]/div[2]/form[1]/div[2]/input[1]").send_keys("123456")
    sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'LOGIN')]").click()
    sleep(2)
    alert = driver.switch_to.alert
    WebDriverWait(driver, 20)
    alert.accept()
    driver.refresh()
    sleep(5)
    return driver


def test_restaurnt():
    driver = test_login()
    driver.find_element(By.XPATH, "//header/form[1]/input[1]").send_keys("paris")
    driver.find_element(By.XPATH, "//header/form[1]/*[1]").send_keys(Keys.ENTER)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'hotels')]")))
    driver.find_element(By.XPATH, "//a[contains(text(),'restaurants')]").click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'hotels')]")))
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/section[1]/section[1]/section[1]/article[1]/a[1]").click()

#page new jawad
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[contains(text(),'hotels')]")))
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/section[1]/section[1]/section[1]/div[1]/button[1]/*[1]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Comments')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Q&A')]").click()

    driver.find_element(By.XPATH, "//a[contains(text(),'Paris')]").click()
    driver.find_element(By.XPATH,"//a[contains(text(),'hotels')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'activities')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'restaurants')]").click()

    driver.find_element(By.XPATH,"//header/div[4]/a[1]").click()
    driver.find_element(By.XPATH,"//a[contains(text(),'About us')]").click()
    driver.find_element(By.XPATH,"//header/div[2]/button[1]/*[1]").click()

    #Profile button
    driver.find_element(By.XPATH,"//header/div[1]/a[1]/div[1]").click()
    #Exit button
    driver.find_element(By.XPATH,"//header/div[1]/button[1]").click()
    alert = driver.switch_to.alert
    alert.accept()
    alert.accept()
    sleep(4)


SORT_BUTTON = '//div[1]/div[1]/button[1]'
SELECT_SORT = '//div[1]/div[1]/select[1]'

def test_sort_options():
    driver = int()
    WebDriverWait(driver, 20)
    sort_button = driver.find_element(By.XPATH, SORT_BUTTON)
    select_sort = Select(driver.find_element(By.XPATH, SELECT_SORT))
    for i in range(7):
        if i != 0:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, SELECT_SORT)))
            select_sort.select_by_index(i)
            driver.implicitly_wait(15)
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, SORT_BUTTON)))
            sort_button.click()
            WebDriverWait(driver, 20)

TOP = 'header'
CENTER = '#mainScroll'
BOTTOM = '//footer[1]/button[1]'
WHO_ARE_WE_DETAILS = '//footer[1]'

def test_ui():
    driver = int()
    top_section = driver.find_element(By.CSS_SELECTOR, TOP).get_attribute('innerText')

    center_section = driver.find_element(By.CSS_SELECTOR, CENTER).get_attribute('innerText')

    who_are_we_details = driver.find_element(By.XPATH, WHO_ARE_WE_DETAILS).get_attribute('innerText')

    assert top_section == "About us\nTripYoetz"

    assert center_section == "Paris\nhotels\nrestaurants\nactivities\nRestaurants\nSort By\nrating high to " \
                             "low\nrating low to high\nprice high to low\nprice low to high\nName" \
                             " A-Z\nName Z-A\nSort\nNew Jawad Longchamp\n30 rue de Longchamp, 75116 Paris," \
                             " France\n\n75$ - 90$\n\n1 reviews\n\nASPIC\n24 rue de la Tour D Auvergne, 75009" \
                             " Paris France\n\n55$ - 95$\n\nno reviews yet\n\nPur' - Jean-François Rouquette\n5" \
                             " Rue de la Paix Park Hyatt Paris, 75002 Paris France\n\n175$ - 240$\n\nno reviews" \
                             " yet\n\nBoutary\n25 rue Mazarine, 75006 Paris France\n\n35$ - 70$\n\nno reviews " \
                             "yet\n\nOrigines\n8 rue du Dragon, 75006 Paris France\n\n39$ - 59$\n\nno reviews " \
                             "yet\n\nBistrot Kinzo\n6 rue de Ponthieu, 75008 Paris France\n\n20$ - 54$\n\nno " \
                             "reviews yet\n\nLa Table de Colette\n17 rue Laplace La Table de colette, 75005 Paris " \
                             "France\n\n39$ - 89$\n\nno reviews yet\n\nDidon\n8 rue du Dragon, 75006 Paris " \
                             "France\n\n20$ - 38$\n\nno reviews yet\n\n114 Faubourg\n114 rue du Faubourg Saint " \
                             "Honore, 75008 Paris France\n\n130$ - 150$\n\nno reviews yet\n\nMoSuke\n11 rue Raymond" \
                             " Losserand, 75014 Paris France\n\n55$ - 110$\n\nno reviews yet"

    assert who_are_we_details == "Marcos Bazbih\n24 years old, Ashdod\nTikva Yosef\n26 years old, " \
                                 "Natanya\nAvi Admaso\n26 years old, Ashdod\nWho are we?\nTripYoetz\nLearn " \
                                 "more\ncopyright © | 2022 TripYoetz | all right reserved."





























