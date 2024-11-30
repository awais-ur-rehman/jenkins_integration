from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Test Case 1: Open Homepage
def test_homepage():
    driver.get("http://localhost:3000") 
    assert "Welcome to Assignment 03" in driver.title, "Homepage title does not contain 'Welcome to Assignment 03'"
    print("Test Case 1 Passed: Homepage loaded successfully.")

# Test Case 2: Form Submission
def test_form_submission():
    driver.get("http://localhost:3000")
    name_field = driver.find_element(By.ID, "name")
    name_field.send_keys("Test User")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    assert "Hello, Test User!" in driver.page_source, "Form submission failed."
    print("Test Case 2 Passed: Form submission successful.")

# Execute Tests
try:
    test_homepage()
    test_form_submission()
finally:
    driver.quit()
