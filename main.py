
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://haveibeenpwned.com/") 
time.sleep(5)

with open("pwned.txt") as f:
	for line in f:
		line = str(line.strip())
		input_field = driver.find_element(By.XPATH, '//*[@id="Account"]')
		input_field.send_keys(line)
		time.sleep(2)
		enter = driver.find_element(By.XPATH, '//*[@id="searchPwnage"]')
		enter.click()
		time.sleep(2)
		response = driver.find_element_by_class_name("pwnTitle").text
		if "Good news — no pwnage found!" in response:
			print(str(line) + " CLEAN!" )
		else:
			print(str(line) + " PWNED!" )
		driver.get("https://haveibeenpwned.com/")		

driver.quit()


