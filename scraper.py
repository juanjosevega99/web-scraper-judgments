from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def scrape_website(file_number):
    # Specify the remote URL where the Selenium server is running
    selenium_url = 'http://localhost:4444/wd/hub'  # Adjust this URL as needed
    url = 'https://consultaprocesos.ramajudicial.gov.co/Procesos/NumeroRadicacion'

    # Additional options for headless mode and other settings
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    # Connect to the remote Selenium server
    driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)

    # Open the target web page
    driver.get(url)

    # Find the input field and enter the number
    input_field = driver.find_element_by_id('input-72')
    input_field.send_keys(file_number)

    # Find the button and click it
    button = driver.find_element_by_xpath("//button[span='Consultar']")
    button.click()

    # Wait for the page to load or for certain elements to be present
    time.sleep(5)  # Example: wait for 5 seconds

    # Perform any additional actions or scrape the data you need
    # ...

    # Close the browser
    driver.quit()
