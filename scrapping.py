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
from credentials import decrypt_credentials
from path import *

username = getpass.getuser()
d = date.today()
d1 = d-timedelta(days=0)
date1 = d1.strftime("%d-%m-%Y")
time.sleep(5)
today = datetime.datetime.today()
username = getpass.getuser()

key = b'Z1IHJtIquAGruPsZjsQhjZJE0Zv9-M3iR1KsQWqm5hg='
encrypted_username = b'gAAAAABl64ZdN0uwCjOn--GDF6MQf7dl2u1Li_2YMMfsoXE32wFh5Ck4RliaUICvKYjvqY66lARxhxxKS6GmcdZd7yyh3oFxcw4IoctdnJVh72hkQ40x61s='
encrypted_password = b'gAAAAABl64ZdHI4BJT1zkHoVzehdp9O9LLvHeKOt8ZY5CACwvnLgUWldUFh42FrXIA1jf6CxxDfi67h-_DQk-L_DfBvtklpfhQ=='

username, password = decrypt_credentials(key, encrypted_username, encrypted_password)


driver = webdriver.Chrome()
driver.get('https://uk.linkedin.com/')

user = driver.find_element(By.ID,"session_key").send_keys(username)
passw = driver.find_element(By.ID,"session_password").send_keys(password)
driver.find_element(By.XPATH,log_submit).click()
time.sleep(5)
driver.find_element(By.XPATH, jobs_button).click()
time.sleep(2)
driver.find_element(By.XPATH,job_input).send_keys("mlops")
time.sleep(2)
driver.find_element(By.XPATH,location_input).send_keys("UNITED KINGDOM")
time.sleep(2)
webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
time.sleep(4)
driver.find_element(By.XPATH,date_posted).click()
time.sleep(2)
driver.find_element(By.XPATH,date_selection).click()
time.sleep(2)
driver.find_element(By.XPATH, results).click()
time.sleep(2)
base_xpath = base_path
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
        driver.execute_command("done")
    Company_name = driver.find_element(By.XPATH, comp_name_xpath).get_attribute("innerHTML")
    print(Company_name)
    time.sleep(2)
    driver.find_element(By.XPATH, job_link_xpath).click()
    time.sleep(4)
    content_1 = driver.find_element(By.XPATH,content_up).get_attribute("innerHTML")
    print("content_1 = "+content_1)
    time.sleep(5)
    content_2 = driver.find_element(By.XPATH, content_down).get_attribute("innerHTML")
    print("content_2" + content_2)
    time.sleep(2)