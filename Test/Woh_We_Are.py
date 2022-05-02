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
    title = driver.find_element(By.XPATH,text_title ).get_attribute("innerText")
    assert title == "TripYoetz\nLearn more\ncopyright © | 2022 TripYoetz | all right reserved."
    details_avi = driver.find_element(By.XPATH, date_A).get_attribute("innerText")
    assert details_avi == "Avi Admaso\n26 years old, Ashdod"
    details_tikva = driver.find_element(By.XPATH,date_T ).get_attribute("innerText")
    assert details_tikva == "Tikva Yosef\n26 years old, Natanya"
    details_marcos = driver.find_element(By.XPATH,date_M ).get_attribute("innerText")
    assert details_marcos == "Marcos Bazbih\n24 years old, Ashdod"

    #button
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//body/div[@id='root']/div[1]/footer[1]/div[1]/a[1]")))
    driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/footer[1]/div[1]/a[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Learn more')]")))
    driver.find_element(By.XPATH, "//a[contains(text(),'Learn more')]").click()

    # # #avi
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,avi_git)))
    driver.find_element(By.XPATH,avi_git).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,avi_linkdin)))
    driver.find_element(By.XPATH,avi_linkdin).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,avi_email)))
    driver.find_element(By.XPATH,avi_email).click()
    # #tikva
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,tikva_git)))
    driver.find_element(By.XPATH,tikva_git).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,tikva_linkdin)))
    driver.find_element(By.XPATH,tikva_linkdin ).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,tikva_email)))
    driver.find_element(By.XPATH, tikva_email).click()
    # #marcos
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,marcos_git)))
    driver.find_element(By.XPATH,marcos_git).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,marcos_linkdin)))
    driver.find_element(By.XPATH,marcos_linkdin).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,marcos_email)))
    driver.find_element(By.XPATH,marcos_email).click()
