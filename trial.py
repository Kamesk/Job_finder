import time
import getpass
from datetime import date, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from credentials import decrypt_credentials
from bs4 import BeautifulSoup
from path import *
import User_input
from content_extractor import token_extractor
from  write import extract_info


job_name = []
company = []
location = []
pay = []
level = []
skill_match = []
employee_no = []
content_1 = []
content_2 = []

class JobScraper:
    def __init__(self):
        self.username = getpass.getuser()
        self.driver = webdriver.Chrome()
        self.driver.get('https://uk.linkedin.com/')
        self.login()

    def login(self):
        username, password = decrypt_credentials(User_input.key, User_input.encrypted_username, User_input.encrypted_password)
        user_input = self.driver.find_element(By.ID, "session_key")
        user_input.send_keys(username)
        pass_input = self.driver.find_element(By.ID, "session_password")
        pass_input.send_keys(password)
        log_button = self.driver.find_element(By.XPATH, log_submit)
        log_button.click()
        time.sleep(5)

    def search_jobs(self):
        self.driver.find_element(By.XPATH, jobs_button).click()
        time.sleep(4)
        job_in = self.driver.find_element(By.XPATH, job_input)
        job_in.send_keys(User_input.user_input1)
        time.sleep(4)
        location_in = self.driver.find_element(By.XPATH, location_input)
        location_in.send_keys(User_input.user_input2)
        time.sleep(2)
        webdriver.ActionChains(self.driver).send_keys(Keys.RETURN).perform()
        time.sleep(4)
        self.driver.find_element(By.XPATH, date_posted).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, date_selection).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, results).click()
        time.sleep(2)

    def scrape_jobs(self):
        # base_xpath = base_path
        num_job_links = 50
        for i in range(1, num_job_links + 1):
            print(i)
            job_link_xpath = f"{base_path}[{i}]/div/div/div[1]/div[2]/div[1]/a"
            job_name_xpath = f"{base_path}[{i}]/div/div/div[1]/div[2]/div[1]/a/strong"
            comp_name_xpath = f"{base_path}[{i}]/div/div/div[1]/div[2]/div[2]/span"    
            pay_d = """//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/ul/li[1]/span/span[1]"""
            level_d = """//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/ul/li[1]/span/span[4]"""
            strength_d = """//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/ul/li[2]/span"""
            skill_compare_d = """//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/ul/li[3]"""
        
            
            try:
                position_name = self.driver.find_element(By.XPATH, job_name_xpath).get_attribute("innerHTML")
                job_name.append(position_name)
                time.sleep(4)
            except NoSuchElementException:
                print("Element not found for job name at index:", i)
                pass
            try:
                company_name = self.driver.find_element(By.XPATH, comp_name_xpath).get_attribute("innerHTML")
                company.append(company_name)
                time.sleep(4)

            except NoSuchElementException:
                print("Job applications done for the Day")
                self.driver.execute_script("alert('Application Done for LinkedIN');")
                self.driver.quit()
            try:     
                self.driver.find_element(By.XPATH, job_link_xpath).click()
            except NoSuchElementException:
                pass
            time.sleep(4)
            try:
                pay_data = self.driver.find_element(By.XPATH, pay_d).get_attribute("innerHTML")
                pay.append(pay_data)
            except NoSuchElementException:
                pass
            time.sleep(2)
            try:
                level_data = self.driver.find_element(By.XPATH, level_d).get_attribute("innerHTML")
                level.append(level_data)
            except NoSuchElementException:
                pass
            time.sleep(2)
            try:    
                strength_data = self.driver.find_element(By.XPATH, strength_d).get_attribute("innerHTML")
                employee_no.append(strength_data)
            except NoSuchElementException:
                pass    
            time.sleep(2)
            try:
                skill_compare_data = self.driver.find_element(By.XPATH, skill_compare_d).get_attribute("innerHTML")
                skill_match.append(skill_compare_data)
            except NoSuchElementException:
                pass
            time.sleep(2)
            # try:
            #     content_1 = self.driver.find_element(By.XPATH, content_up).get_attribute("innerHTML")
            # except NoSuchElementException:
            #     pass    
            # time.sleep(5)
            # try:
            #     content_2 = self.driver.find_element(By.XPATH, content_down).get_attribute("innerHTML")
            # except NoSuchElementException:
            #     pass    
            # time.sleep(5)
            # stripped_data = token_extractor(content_1, content_2)
            # extracted_infos = extract_info(stripped_data)
                
            print(company,job_name,pay,level,employee_no,skill_match)
            
    def close(self):
        self.driver.quit()

# if __name__ == "__main__":
scraper = JobScraper()
scraper.search_jobs()
scraper.scrape_jobs()
scraper.close()