from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

url = "https://id.atlassian.com/login?continue=https%3A%2F%2Fid.atlassian.com%2Fjoin%2Fuser-access%3Fresource%3Dari%253Acloud%253Ajira%253A%253Asite%252F42dba59f-cb48-493f-a34b-2bfd62ac3f65%26continue%3Dhttps%253A%252F%252Fcfainstitute.atlassian.net%252Fjira%252Fservicedesk%252Fprojects%252FITHD%252Fqueues%252Fcustom%252F433&application=jira"  # Replace with your Jira login URL
driver.get(url)

time.sleep(10)

email_input = driver.find_element("id", "username")  # Adjust if necessary
email_input.send_keys("samidh.darji@cfainstitute.in") 

time.sleep(10)