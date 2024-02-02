from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv
executable_path = 'C:/Users/DIVYAJOTHI M/Downloads/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(executable_path)
wait = WebDriverWait(driver, 20)


driver.get("https://www.naukri.com/for-engineering-and-technology-pharmacy-management-jobs")

count = 100  

index, new_index, i = '0', 1, 0  
required_post_xpath = '(//*[@class="jobTuple bgWhite br4 mb-8"])['+index+']/div/div/a'
link_xpath = '(//*[@class="jobTuple bgWhite br4 mb-8"])['+index+']/div/div/a'
company_xpath = '(//*[@class="jobTuple bgWhite br4 mb-8"])['+index+']/div/div/div/a'
experience_xpath = '(//*[@class="jobTuple bgWhite br4 mb-8"])['+index+']/div/div/ul/li[1]/span'
salary_xpath = '(//*[@class="jobTuple bgWhite br4 mb-8"])['+index+']/div/div/ul/li[2]/span'

csv_file = open('Naukri_scrape.csv', 'a', encoding="utf-8", newline='')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Required post', 'Company', 'Vacancy Link', 'Experience Needed', 'Salary'])

while i < count:

    for j in range(20):
        
        temp_index = str(new_index).zfill(2)  
        required_post_xpath = required_post_xpath.replace(index, temp_index)
        link_xpath = link_xpath.replace(index, temp_index)
        company_xpath = company_xpath.replace(index, temp_index)
        experience_xpath = experience_xpath.replace(index, temp_index)
        salary_xpath = salary_xpath.replace(index, temp_index)
        index = str(new_index).zfill(2)
        try:
            
            required_post= wait.until(EC.presence_of_element_located((By.XPATH, required_post_xpath))).text
            print(required_post)
        except:
            required_post = "NULL"
        try:
            link = wait.until(EC.presence_of_element_located((By.XPATH, link_xpath))).get_attribute('href')
            print(link)
        except:
            link = "NULL"
        try:
            company = wait.until(EC.presence_of_element_located((By.XPATH, company_xpath))).text
            print(company)
        except:
            subheading = "NULL"
        try:
            experience = wait.until(EC.presence_of_element_located((By.XPATH, experience_xpath))).text
            print(experience)
        except:
            experience = "NULL"
        try:
            salary = wait.until(EC.presence_of_element_located((By.XPATH, salary_xpath))).text
            print(salary)
        except:
            salary = "Not Disclosed"
        new_index += 1
        i += 1
        print("--------------------------- "+str(i)+" ----------------------------------")

        csv_writer.writerow([required_post, company, link, experience, salary])
        if i >= count:
            break
    if i >= count:
        break
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Next"]'))).click()
    new_index = 1
csv_file.close()

