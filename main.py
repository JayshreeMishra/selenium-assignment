from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--incognito")

driver_path = r"C:\Users\jaysh\OneDrive\Desktop\Selenium-assignment\edgedriver_win64\msedgedriver.exe"
service = Service(driver_path)
driver = webdriver.Edge(service=service, options=options)

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform")



# Full Name
full_name_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @jsname='YPqjbf']"))
)
full_name_element.send_keys("Jayshree Rajesh Mishra")

#Contact Number
contact_number_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@jsname='YPqjbf' and @aria-labelledby='i5']"))
)
contact_number_element.send_keys("9766082151")

#Email ID
email_id_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@jsname='YPqjbf' and @aria-labelledby='i9']"))
)
email_id_element.send_keys("jayshreemishra197@gmail.com")

# Full Address
full_address_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//textarea[@jsname='YPqjbf' and @aria-labelledby='i13']"))
)
full_address_element.send_keys("Near Sunny Palace, Adarsh Nagar, Khamgaon")

# Pin Code
pin_code_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@jsname='YPqjbf' and @aria-labelledby='i17']"))
)
pin_code_element.send_keys("444303")

# Date of Birth
date_of_birth_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='date' and @jsname='YPqjbf']"))
)
date_of_birth_element.send_keys("19-05-2001")

# Gender
gender_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @jsname='YPqjbf' and @aria-labelledby='i26']"))
)
gender_element.send_keys("Female")

# Verification Code
verification_code_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @jsname='YPqjbf' and @aria-labelledby='i30']"))
)
verification_code_element.send_keys("GNFPYC")

time.sleep(30)

# Close the browser
#driver.quit()

# Submit the form
#submit_button = WebDriverWait(driver, 30).until(
# EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and @jsname='M2UYVd']")))
#submit_button.click()