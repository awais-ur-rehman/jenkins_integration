from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Test Case 1: Open Homepage
def test_homepage():
    driver.get("http://localhost:80")  # Ensure the server is running
    assert "Welcome to Assignment 03" in driver.title, "Homepage title does not contain 'Welcome to Assignment 03'"
    print("Test Case 1 Passed: Homepage loaded successfully.")

# Test Case 2: Form Submission
def test_form_submission():
    driver.get("http://localhost:80")
    # Locate the input field by its ID
    name_field = driver.find_element(By.ID, "name")
    name_field.send_keys("Test User")  # Enter a name in the form
    # Locate the submit button and click it
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)  # Wait for the server response
    assert "Hello, Test User!" in driver.page_source, "Form submission failed."
    print("Test Case 2 Passed: Form submission successful.")

# Execute Tests
try:
    test_homepage()
    test_form_submission()
finally:
    driver.quit()
