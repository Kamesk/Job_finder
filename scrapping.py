from collections import OrderedDict
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import re
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from write import *

username = getpass.getuser()
d = date.today()
d1 = d-timedelta(days=0)
date1 = d1.strftime("%d-%m-%Y")
time.sleep(5)
today = datetime.datetime.today()
username = getpass.getuser()


driver = webdriver.Chrome()
driver.get('https://uk.linkedin.com/')
username = "fallforwardkk@gmail.com"
password="MYlinkedin29"

user = driver.find_element(By.ID,"session_key").send_keys(username)
passw = driver.find_element(By.ID,"session_password").send_keys(password)
driver.find_element(By.XPATH,"""/html/body/main/section[1]/div/div/form/div[2]/button""").click()
time.sleep(5)
driver.find_element(By.XPATH, """/html/body/div[6]/header/div/nav/ul/li[3]/a/span""").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]").send_keys("mlops")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[6]/header/div/div/div/div[2]/div[3]/div/div/input[1]").send_keys("UNITED KINGDOM")
time.sleep(2)
webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
time.sleep(4)
driver.find_element(By.XPATH,"""/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[3]/div/span/button""").click()
time.sleep(2)
driver.find_element(By.XPATH,"""/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[3]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[4]/label""").click()
time.sleep(2)
driver.find_element(By.XPATH, """/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[3]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]""").click()
time.sleep(2)
base_xpath = "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li"
num_job_links = 50
for i in range(1, num_job_links + 1):
    # Construct the XPath for the current job link
    job_link_xpath = f"{base_xpath}[{i}]/div/div/div[1]/div[2]/div[1]/a"
    job_name_xpath = f"{base_xpath}[{i}]/div/div/div[1]/div[2]/div[1]/a/strong"
    comp_name_xpath = f"{base_xpath}[{i}]/div/div/div[1]/div[2]/div[2]/span"
    try:
        position_name = driver.find_element(By.XPATH, job_name_xpath).get_attribute("innerHTML")
        print(position_name)
        time.sleep(2)
    except NoSuchElementException:
        
    Company_name = driver.find_element(By.XPATH, comp_name_xpath).get_attribute("innerHTML")
    print(Company_name)
    time.sleep(2)
    driver.find_element(By.XPATH, job_link_xpath).click()
    time.sleep(4)
    content_1 = driver.find_element(By.XPATH,"""//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]""").get_attribute("innerHTML")
    print("content_1 = "+content_1)
    time.sleep(5)
    content_2 = driver.find_element(By.XPATH, """//*[@id="job-details"]/span""").get_attribute("innerHTML")
    print("content_2" + content_2)
    time.sleep(2)