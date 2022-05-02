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
