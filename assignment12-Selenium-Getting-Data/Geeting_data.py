import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Chrome and ChromeDriver paths
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHROMEDRIVER_PATH = r"C:\Users\kaugs\OneDrive\Desktop\Tutedude\Chrom_Testing\chromwin64\chrome_driver\chromedriver (1).exe"


# Configure Chrome
options = Options()
options.binary_location = CHROME_PATH

# Configure ChromeDriver
service = Service(CHROMEDRIVER_PATH)

# Create Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)

# Maximize the browser window
driver.maximize_window()
try:

    # 1. Open Google and perform a search
   
    driver.get("https://www.google.com")
    time.sleep(3)

    # Find search box using NAME

    search_box = driver.find_element(By.NAME, "q")

    # Enter search query and submit

    search_box.send_keys("Selenium")
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    time.sleep(4)
    print("Google search completed.")

    # 2. Navigate back to Google
  
    driver.back()
    time.sleep(3)
    print("Navigated back to Google.")

    # 3. Open Amazon

    driver.get("https://www.amazon.com")
    time.sleep(5)
    print("Amazon opened.")

    # 4. Click element using CLASS_NAME
  
    try:
        driver.find_element(By.CLASS_NAME,"a-button-input").click()
        print("Button clicked using CLASS_NAME.")
        time.sleep(3)
    except Exception:
        print("Class-name button was not available. Continuing...")

    # 5. Click element using LINK_TEXT

    try:
        driver.find_element(By.LINK_TEXT,"Today's Deals").click()
        print("Today's Deals clicked.")
        time.sleep(4)
    except Exception:
        print("Today's Deals link was not available. Continuing...")

    # 6. Refresh the page

    driver.refresh()
    time.sleep(3)
    print("Amazon page refreshed.")

    # 7. Search for Gaming Laptop using XPATH
   
    search = driver.find_element(
        By.XPATH,
        '//input[@id="twotabsearchtextbox"]')
    search.send_keys("Gaming Laptop")
    time.sleep(2)

    # Click search button using XPATH

    driver.find_element(
        By.XPATH,
        '//input[@id="nav-search-submit-button"]').click()
    time.sleep(5)
    print("Gaming Laptop search completed.")

    # 8. Extract data using XPATH
 
    items = driver.find_elements(
        By.XPATH,
        '//h2[@class="a-size-medium a-spacing-none a-color-base a-text-normal"]')
    total = len(items)
    print()
    print(str(total) + " items found")
    print("-" * 60)

    # 9. Display extracted data

    for index, item in enumerate(items, start=1):
        title = item.text.strip()
        if title:
            print(f"Item No.{index} - {title[:50]}")
    print("-" * 60)
    print("Data extraction completed.")
    time.sleep(5)
finally:
    # 10. Close browser

    driver.quit()
    print("Browser closed successfully.")

