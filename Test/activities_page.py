from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def init():
    driver = webdriver.Chrome("..//Driver/chromedriver.exe")
    driver.get("https://trip-yoetz.herokuapp.com/activities")
    driver.maximize_window()
    return driver

# test trensfer other pages using navbar from activities page
def test_trensfer_other_pages_by_navbar():
    driver = init()
    loggin = "//a[contains(text(),'Login')]"
    register = "//a[contains(text(),'Register')]"
    about = "//a[contains(text(),'About us')]"
    trip_yoetz = "//header/div[4]/a[1]"
    loginMsg_path = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[1]"
    register_path = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[1]"
    about_path = "//body/div[@id='root']/div[1]/section[1]/section[1]/div[2]"
    tripMsg_path = "//body/div[@id='root']/div[1]/section[1]/section[1]/form[1]"
    about_innerText = "About Us\nTripYoetz, the world's largest travel guidance platform, helps hundreds of millions of people each month become better travelers, from planning to booking to taking a trip. Travelers across the globe use the Tripadvisor site and app to discover where to stay, what to do and where to eat based on guidance from those who have been there before. With more than 1 billion reviews and opinions of nearly 8 million businesses, travelers turn to Tripadvisor to find deals on accommodations, book experiences, reserve tables at delicious restaurants and discover great places nearby. As a travel guidance company available in 43 markets and 22 languages, Tripadvisor makes planning easy no matter the trip type."
    driver.find_element(By.XPATH,loggin).click()
    loginMsg = driver.find_element(By.XPATH, loginMsg_path).get_attribute("innerText")
    assert loginMsg == "New here ?\nTo register please click the link below\nRegister"
    driver.back()
    driver.find_element(By.XPATH,register).click()
    register = driver.find_element(By.XPATH,register_path).get_attribute("innerText")
    assert register == "Already a member ?\nTo login please click the link below\nLogin"
    driver.back()
    driver.find_element(By.XPATH,about).click()
    about = driver.find_element(By.XPATH,about_path).get_attribute("innerText")
    assert about == about_innerText
    driver.find_element(By.XPATH,"//header/div[4]/a[1]").click()
    driver.back()
    sleep(1)
    driver.find_element(By.XPATH,trip_yoetz).click()
    tripMsg = driver.find_element(By.XPATH,tripMsg_path).get_attribute("innerText")
    assert tripMsg == ""


# test search in nav bar incorrect with empty fields, Special Characters,numbers ,invalid city
def test_search_in_nav_bar_incorrect():
    driver = init()
    errorMsg_path = "//h2[contains(text(),'no city found')]"
    values = ["pari","1234","%#%@!!",""]
    input = driver.find_element(By.XPATH,"//header/form[1]/input[1]")
    for i in range(len(values)):
        input.send_keys(values[i])
        input.send_keys(Keys.ENTER)
        input.clear()
        WebDriverWait(driver,1).until(EC.presence_of_element_located((By.XPATH,errorMsg_path)))
        errorMsg = driver.find_element(By.XPATH,errorMsg_path).get_attribute("innerText")
        assert errorMsg == "No City Found"

# test search city correct
def test_search_in_navbar_city_correct():
    driver = init()
    parisMsg_path = "//h1[@class='city-name-h1']"
    search = driver.find_element(By.XPATH,"//header/form[1]/input[1]")
    search.send_keys("paris")
    search.send_keys(Keys.ENTER)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, parisMsg_path)))
    parisMsg = driver.find_element(By.XPATH,parisMsg_path).get_attribute("innerText")
    assert parisMsg == "Discover Paris"




# verify that the nav bar ui is comptible with the disghn document
def test_ui_for_top_page():
    driver = init()
    login_register_path = driver.find_element(By.XPATH,"//header/div[1]").get_attribute("innerText")
    assert login_register_path == "Login\nRegister"
    about_us_path = driver.find_element(By.XPATH,"//a[contains(text(),'About us')]").get_attribute("innerText")
    assert about_us_path == "About us"
    trip_yoetz_logo_path = driver.find_element(By.XPATH,"//header/div[4]/a[1]").get_attribute("innerText")
    assert trip_yoetz_logo_path =="TripYoetz"

# verify that the center of the page ui is compatible with the design document

def test_ui_for_center_page():
    driver = init()
    search = driver.find_element(By.XPATH, "//header/form[1]/input[1]")
    search.send_keys("paris")
    search.send_keys(Keys.ENTER)
    sleep(2)
    activities_path = "//a[contains(text(),'activities')]"
    WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,activities_path)))
    driver.find_element(By.XPATH,activities_path).click()
    sleep(2)
    center_path = "//body/div[@id='root']/div[1]/section[1]/section[1]/section[1]/article[1]/div[1]"
    center = driver.find_element(By.XPATH,center_path).get_attribute("innerText")
    assert center == "Eiffel dfs\n5 Avenue Anatole France, 75007 Paris France\n\n85$ - 120$\n\n1 reviews"



# verify that the bottom of the page (who we are)  ui is compatible with the design document
def test_ui_for_bottom_page():
    driver = init()
    bottom_path = "//div[1]/footer[1]"
    bottom_text = "Marcos Bazbih\n24 years old, Ashdod\nTikva Yosef\n26 years old, Natanya\nAvi Admaso\n26" \
            " years old, Ashdod\nWho are we?\nTripYoetz\nLearn more\ncopyright" \
            " © | 2022 TripYoetz | all right reserved."
    bottom = driver.find_element(By.XPATH, bottom_path).get_attribute('innerText')
    assert bottom == bottom_text













