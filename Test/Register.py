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


text_register = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[1]"
#register_buttons
def test_buttons():
    driver = int()
    driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'Register')]").click()
    #text-UI
    value = driver.find_element(By.XPATH,text_register ).get_attribute("innerText")
    assert value == "Already a member ?\nTo login please click the link below\nLogin"

    driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
    driver.find_element(By.XPATH,"//header/div[2]/button[1]/*[1]").click()
    driver.find_element(By.XPATH,"//header/div[3]").click()
    driver.find_element(By.XPATH,"//header/div[4]/a[1]").click()
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/footer[1]/button[1]").click()
    driver.find_element(By.XPATH,"//header/form[1]/input[1]").send_keys("paris")
    driver.find_element(By.XPATH,"//header/form[1]/*[1]").send_keys(Keys.ENTER)

first_name = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[2]/form[1]/div[1]/input[1]"
last_name = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[2]/form[1]/div[2]/input[1]"
email = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[2]/form[1]/div[4]/input[1]"
password = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[2]/form[1]/div[6]/input[1]"
confirm = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[2]/form[1]/div[7]/input[1]"
show_pass = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[2]/form[1]/div[7]/button[1]/*[1]"


#test - proper registration
def test1():
    driver = int()
    driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
    a = driver.find_elements(By.XPATH, "//input")
    for i in range(len(a)):
        if i == 1:
            a[i].send_keys('jonathan')
        elif i == 2:
            a[i].send_keys('elias')
        elif i == 3:
            driver.execute_script("document.getElementsByClassName('register-input')[2].value = '1994-06-10'")
        elif i == 4:
            a[i].send_keys('gonathan46@gmail.com')
        elif i == 5:
            a[i].send_keys('jona')
        elif i == 6:
            a[i].send_keys('123456')
        elif i == 7:
            a[i].send_keys('123456')
    driver.find_element(By.XPATH,show_pass).click()
    driver.find_element(By.XPATH,"//button[contains(text(),'REGISTER')]").click()
#Register without entering "name"
def test2():
    driver = int()
    driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()
    a = driver.find_elements(By.XPATH, "//input")
    for i in range(len(a)):
        if i == 1:
            a[i].send_keys('')
        elif i == 2:
            a[i].send_keys('elias')
        elif i == 3:
            driver.execute_script("document.getElementsByClassName('register-input')[2].value = '1994-06-10'")
        elif i == 4:
            a[i].send_keys('gonathan46@gmail.com')
        elif i == 5:
            a[i].send_keys('jona')
        elif i == 6:
            a[i].send_keys('123456')
        elif i == 7:
            a[i].send_keys('123456')
    driver.find_element(By.XPATH, show_pass).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'REGISTER')]").click()
    sleep(5)
#Register without entering "Last Name"
def test3():
    driver = int()
    driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()
    a = driver.find_elements(By.XPATH, "//input")
    for i in range(len(a)):
        if i == 1:
            a[i].send_keys('jonathan')
        elif i == 2:
            a[i].send_keys('')
        elif i == 3:
            driver.execute_script("document.getElementsByClassName('register-input')[2].value = '1994-06-10'")
        elif i == 4:
            a[i].send_keys('gonathan46@gmail.com')
        elif i == 5:
            a[i].send_keys('jona')
        elif i == 6:
            a[i].send_keys('123456')
        elif i == 7:
            a[i].send_keys('123456')
    driver.find_element(By.XPATH, show_pass).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'REGISTER')]").click()
#Register without entering "Date of birth"
def test4():
    driver = int()
    driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()
    a = driver.find_elements(By.XPATH, "//input")
    for i in range(len(a)):
        if i == 1:
            a[i].send_keys('jonathan')
        elif i == 2:
            a[i].send_keys('elias')
        elif i == 3:
            driver.execute_script("document.getElementsByClassName('register-input')[2].value = ''")
        elif i == 4:
            a[i].send_keys('gonathan46@gmail.com')
        elif i == 5:
            a[i].send_keys('jona')
        elif i == 6:
            a[i].send_keys('123456')
        elif i == 7:
            a[i].send_keys('123456')
    driver.find_element(By.XPATH, show_pass).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'REGISTER')]").click()
#Register without entering an email
def test5():
    driver = int()
    driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()
    a = driver.find_elements(By.XPATH, "//input")
    for i in range(len(a)):
        if i == 1:
            a[i].send_keys('jonathan')
        elif i == 2:
            a[i].send_keys('elias')
        elif i == 3:
            driver.execute_script("document.getElementsByClassName('register-input')[2].value = '1994-06-10'")
        elif i == 4:
            a[i].send_keys('')
        elif i == 5:
            a[i].send_keys('jona')
        elif i == 6:
            a[i].send_keys('123456')
        elif i == 7:
            a[i].send_keys('123456')
    driver.find_element(By.XPATH, show_pass).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'REGISTER')]").click()
#Register without entering password
def test6():
    driver = int()
    driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()
    a = driver.find_elements(By.XPATH, "//input")
    for i in range(len(a)):
        if i == 1:
            a[i].send_keys('jonathan')
        elif i == 2:
            a[i].send_keys('elias')
        elif i == 3:
            driver.execute_script("document.getElementsByClassName('register-input')[2].value = '1994-06-10'")
        elif i == 4:
            a[i].send_keys('gonathan46@gmail.com')
        elif i == 5:
            a[i].send_keys('jona')
        elif i == 6:
            a[i].send_keys('')
        elif i == 7:
            a[i].send_keys('123456')
    driver.find_element(By.XPATH, show_pass).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'REGISTER')]").click()
#Register without entering confirm password
def test7():
    driver = int()
    driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()
    a = driver.find_elements(By.XPATH, "//input")
    for i in range(len(a)):
        if i == 1:
            a[i].send_keys('jonathan')
        elif i == 2:
            a[i].send_keys('elias')
        elif i == 3:
            driver.execute_script("document.getElementsByClassName('register-input')[2].value = '1994-06-10'")
        elif i == 4:
            a[i].send_keys('gonathan46@gmail.com')
        elif i == 5:
            a[i].send_keys('jona')
        elif i == 6:
            a[i].send_keys('123456')
        elif i == 7:
            a[i].send_keys('')
    driver.find_element(By.XPATH, show_pass).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'REGISTER')]").click()
#Register without entering profile image
def test8():
    driver = int()
    driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()
    a = driver.find_elements(By.XPATH, "//input")
    for i in range(len(a)):
        if i == 1:
            a[i].send_keys('jonathan')
        elif i == 2:
            a[i].send_keys('elias')
        elif i == 3:
            driver.execute_script("document.getElementsByClassName('register-input')[2].value = '1994-06-10'")
        elif i == 4:
            a[i].send_keys('gonathan46@gmail.com')
        elif i == 5:
            a[i].send_keys('')
        elif i == 6:
            a[i].send_keys('123456')
        elif i == 7:
            a[i].send_keys('123456')
    driver.find_element(By.XPATH, show_pass).click()
    driver.find_element(By.XPATH, "//button[contains(text(),'REGISTER')]").click()







