from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def init():
    driver = webdriver.Chrome("..//Driver/chromedriver.exe")
    driver.get("https://trip-yoetz.herokuapp.com/")
    driver.maximize_window()

    return driver


def test_all_accessibility_buttons():
    accsesibility_button = "//header/div[2]/button[1]"
    color1_path = "//header/div[2]/div[1]/button[1]"
    color1 = "//header/div[2]/div[1]/button[1]"
    color2_path = "//header/div[2]/button[1]"
    color2 =  "//header/div[2]/div[1]/button[2]"
    color3_path =  "//header/div[2]/button[1]"
    color3 = "//header/div[2]/div[1]/button[3]"
    color4_path =  "//header/div[2]/button[1]"
    color4 = "//header/div[2]/div[1]/button[4]"
    driver = init()
    driver.find_element(By.XPATH, accsesibility_button).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, color1_path)))
    driver.find_element(By.XPATH,color1).click()
    driver.find_element(By.XPATH,color2_path).click()
    WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, color2)))
    driver.find_element(By.XPATH, color2).click()
    driver.find_element(By.XPATH,color3_path).click()
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,color3)))
    driver.find_element(By.XPATH,color3).click()
    WebDriverWait(driver,3)
    driver.find_element(By.XPATH, color4_path).click()
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,color4)))
    driver.find_element(By.XPATH,color4).click()













