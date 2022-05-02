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


# def test_profile():
#     driver = int()
#     # test_login()
#     #כפתור פרופיל
#     WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//header/div[1]/a[1]/img[1]")))
#     driver.find_element(By.XPATH,"//header/div[1]/a[1]/img[1]").click()
#     #כפתור נגישות
#     driver.find_element(By.XPATH,"//header/div[2]/button[1]").click()
    # driver.find_element(By.XPATH,"").click()
    # driver.find_element(By.XPATH,"").click()
    # driver.find_element(By.XPATH,"").click()
    # driver.find_element(By.XPATH,"").click()
    # driver.find_element(By.XPATH,"").click()
    # #כפתור יציאה
    # driver.find_element(By.XPATH,"//header/div[1]/button[1]").click()

avi_git = "//body/div[@id='root']/div[1]/footer[1]/article[3]/div[1]/a[3]/*[1]"
avi_linkdin = "//body/div[@id='root']/div[1]/footer[1]/article[3]/div[1]/a[2]/*[1]"
avi_email = "//body/div[@id='root']/div[1]/footer[1]/article[3]/div[1]/a[1]/*[1]"

tikva_git =  "//body/div[@id='root']/div[1]/footer[1]/article[2]/div[1]/a[3]/*[1]"
tikva_linkdin = "//body/div[@id='root']/div[1]/footer[1]/article[2]/div[1]/a[2]/*[1]"
tikva_email = "//body/div[@id='root']/div[1]/footer[1]/article[2]/div[1]/a[1]/*[1]"

marcos_git =  "//body/div[@id='root']/div[1]/footer[1]/article[1]/div[1]/a[3]/*[1]"
marcos_linkdin = "//body/div[@id='root']/div[1]/footer[1]/article[1]/div[1]/a[2]/*[1]"
marcos_email = "//body/div[@id='root']/div[1]/footer[1]/article[1]/div[1]/a[1]/*[1]"

text_title ="//body/div[@id='root']/div[1]/footer[1]/div[1]"
date_A = "//body/div[@id='root']/div[1]/footer[1]/article[3]"
date_T = "//body/div[@id='root']/div[1]/footer[1]/article[2]"
date_M = "//body/div[@id='root']/div[1]/footer[1]/article[1]"

def test_who_we_are():
    driver = int()
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/footer[1]/button[1]").click()
    #text - UI
    # title = driver.find_element(By.XPATH,text_title ).get_attribute("innerText")
    # assert title == "TripYoetz\nLearn more\ncopyright © | 2022 TripYoetz | all right reserved."
    # details_avi = driver.find_element(By.XPATH, date_A).get_attribute("innerText")
    # assert details_avi == "Avi Admaso\n26 years old, Ashdod"
    # details_tikva = driver.find_element(By.XPATH,date_T ).get_attribute("innerText")
    # assert details_tikva == "Tikva Yosef\n26 years old, Natanya"
    # details_marcos = driver.find_element(By.XPATH,date_M ).get_attribute("innerText")
    # assert details_marcos == "Marcos Bazbih\n24 years old, Ashdod"
    #Not working
    # "Trip yoetz" button
    # driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/footer[1]/div[1]/a[1]").click()
    # sleep(2)
    # "Learn more" button
    # driver.find_element(By.XPATH,"Learn more").click()
    # sleep(2)
    # # #avi
    # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,avi_git)))
    # driver.find_element(By.XPATH,avi_git).click()
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,avi_linkdin)))
    # driver.find_element(By.XPATH,avi_linkdin).click()
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,avi_email)))
    # driver.find_element(By.XPATH,avi_email).click()
    # # #tikva
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,tikva_git)))
    # driver.find_element(By.XPATH,tikva_git).click()
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,tikva_linkdin)))
    # driver.find_element(By.XPATH,tikva_linkdin ).click()
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,tikva_email)))
    # driver.find_element(By.XPATH, tikva_email).click()
    # # #marcos
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,marcos_git)))
    # driver.find_element(By.XPATH,marcos_git).click()
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,marcos_linkdin)))
    # driver.find_element(By.XPATH,marcos_linkdin).click()
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,marcos_email)))
    # driver.find_element(By.XPATH,marcos_email).click()

# def test_Accessibility():


     #
     # driver = int()
     # # driver = test_login()
     # driver.find_element(By.XPATH,"//header/div[2]/button[1]/*[1]").click()
     # n = driver.find_element(By.XPATH,"//header/div[2]/button[1]")
     # for i in range(len(n)):
     #     if i == 0:
     #        n[i].click()
     #
     # sleep(2)

     # driver.find_element(By.XPATH,"//header/div[2]/div[1]/button[2]").click()
     # sleep(2)
     # driver.find_element(By.XPATH,"//header/div[2]/div[1]/button[3]").click()
     # sleep(2)
     # # driver.find_element(By.XPATH,"//header/div[2]/div[1]/button[4]").click()
     # sleep(2)

#     driver = int()
#     driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
#     b = driver.find_elements(By.XPATH, "//a")
#     for i in range(len(b)):
#         if i == 0:
#             b[i].click()
#         elif i == 2:
#             b[i].click()
#         elif i == 3:
#             b[i].click()
#         elif i == 4:
#             b[i].click()


#     driver = int()
#     driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
#     b = driver.find_elements(By.XPATH, "//a")
#     for i in range(len(b)):
#         if i == 0:
#             b[i].click()
#         elif i == 2:
#             b[i].click()
#         elif i == 3:
#             b[i].click()
#         elif i == 4:
#             b[i].click()

# def test_restaurnt():
#     driver = test_login()
#     driver.find_element(By.XPATH, "//header/form[1]/input[1]").send_keys("paris")
#     driver.find_element(By.XPATH, "//header/form[1]/*[1]").send_keys(Keys.ENTER)
#     driver.find_element(By.XPATH, "//a[contains(text(),'restaurants')]").click()
#     driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/section[1]/section[1]/section[1]/article[1]/a[1]").click()
#
#     driver.find_element(By.XPATH, "//button[contains(text(),'Comments')]").click()
#     driver.find_element(By.XPATH, "//button[contains(text(),'Q&A')]").click()
#     driver.find_element(By.XPATH, "Visit here").click()
#     driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/section[1]/section[1]/section[1]/div[1]/button[1]").click()
    # driver.find_element(By.XPATH, "").click()
    # driver.find_element(By.XPATH, "").click()
    # driver.find_element(By.XPATH, "").click()
    # driver.find_element(By.XPATH, "").click()
    # driver.find_element(By.XPATH, "").click()
    # driver.find_element(By.XPATH, "").click()
    # driver.find_element(By.XPATH, "").click()
    # driver.find_element(By.XPATH, "").click()
    # sleep(5)


def test_Paris():
    driver = test_login()
    driver.find_element(By.XPATH,"//header/form[1]/input[1]").send_keys("paris")
    driver.find_element(By.XPATH,"//header/form[1]/*[1]").send_keys(Keys.ENTER)
    #Text -UI
    # article = driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/section[1]/section[1]").get_attribute("innerText")
    # assert article =="Discover Paris\nParis\nhotels\nrestaurants\nactivities\nParis, city and capital of France, situated in the north-central part of the country. People were living on the site of the present-day city, located along the Seine River some 233 miles (375 km) upstream from the river’s mouth on the English Channel (La Manche), by about 7600 BCE. The modern city has spread from the island (the Île de la Cité) and far beyond both banks of the Seine.\nEat\nQuintessential Paris restaurants, bars, and beyond.\nview all\nNew Jawad Longchamp\nASPIC\nPur' - Jean-François Rouquette\nBoutary\nOrigines\nBistrot Kinzo\nview all\nStay\nA mix of the charming, iconic, and modern.\nview all\nview all\nDo\nPlaces to see, ways to wander, and signature experiences that define Paris.\nview all\nEiffel dfs\nview all"
    driver.find_element(By.XPATH, "//a[contains(text(),'hotels')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'restaurants')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'activities')]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Paris')]").click()
    #Scroll buttons
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/section[1]/section[1]/div[1]/button[1]/*[1]").click()
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/section[1]/section[1]/div[1]/button[2]/*[1]").click()
    #view_all buttons
    driver.find_element(By.XPATH,"//body/div[@id='root']/div[1]/section[1]/section[1]/div[1]/div[1]/a[1]").click()
    driver.find_element(By.XPATH, "//a[contains(text(),'Paris')]").click()
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


#ללואה לחיפוש-דוגמה
# def test1():
#     driver = int()
#     a = driver.find_elements(By.XPATH, "//input")
#     for i in range(len(a)):
#         if i == 1:
#             a[i].send_keys('jona')
#         elif i == 2:
#             a[i].send_keys('GTY')
#         sleep(5)
#         a[i].send_keys('Elias')

#לחצנים להרשמה -
# def test10():
#     driver = int()
#     driver.find_element(By.XPATH,"//a[contains(text(),'Register')]").click()
#     b = driver.find_elements(By.XPATH, "//a")
#     for i in range(len(b)):
#         if i == 0:
#             b[i].click()
#             sleep(2)
#         elif i == 1:
#             b[i].click()
#             sleep(2)
#         elif i == 2:
#             b[i].click()
#             sleep(2)
#         elif i == 3:
#             b[i].click()
#             sleep(2)
        # elif i == 4:
        #     b[i].click()
        #     sleep(4)

#לחצנים פריס
# def test11():
#     driver = test_login()
#     driver.find_element(By.XPATH,"//header/form[1]/input[1]").send_keys("paris")
#     driver.find_element(By.XPATH,"//header/form[1]/*[1]").send_keys(Keys.ENTER)
#
#     c = driver.find_elements(By.XPATH, "//a")
#     # WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"paris")))
#     # driver.find_element(By.XPATH,"paris").click()
#     for i in range(len(c)):
#         if i == 0:
#             c[i].click()
#             sleep(2)
#         elif i == 1:
#             c[i].click()
#             sleep(3)


