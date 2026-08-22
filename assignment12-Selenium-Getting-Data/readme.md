# Assignment 12 - Selenium Web Automation
## Problem Statement
Create Python scripts using Selenium WebDriver to automate browser actions and extract data from websites.
# Objective

The objective of this assignment is to use Selenium WebDriver with Python to automate browser actions, interact with web page elements, perform searches, navigate between pages, refresh pages, and extract data from websites.

## Technologies Used

- Python
- Selenium WebDriver
- Google Chrome
- ChromeDriver

## Installation

Install Selenium using the following command:

```bash
pip install selenium
Program Description

The program uses Selenium WebDriver to automate Google and Amazon.

The following operations are performed:

Create a Chrome WebDriver instance using webdriver.Chrome().
Maximize the browser window using driver.maximize_window().
Open Google using driver.get().
Locate the Google search box using By.NAME.
Search for "Selenium" using send_keys().
Use Keys.RETURN to perform the search.
Navigate back using driver.back().
Open Amazon using driver.get().
Locate an element using By.CLASS_NAME.
Click "Today's Deals" using By.LINK_TEXT.
Refresh the Amazon page using driver.refresh().
Locate the Amazon search box using By.XPATH.
Search for "Gaming Laptop".
Click the search button using XPath.
Extract multiple products using find_elements().
Display the extracted product information using print().
Use time.sleep() for wait handling.
Close the browser using driver.quit().
Selenium Locators Used

The following Selenium locators are used in the program:

By.NAME

Used to locate the Google search box.

driver.find_element(By.NAME, "q")
By.CLASS_NAME

Used to locate an element on Amazon.

driver.find_element(By.CLASS_NAME, "a-button-input")
By.LINK_TEXT

Used to locate and click the "Today's Deals" link.

driver.find_element(By.LINK_TEXT, "Today's Deals")
By.XPATH

Used to locate the Amazon search box and search button.

driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')
Important Selenium Methods Used

The following Selenium methods are demonstrated:

webdriver.Chrome()
driver.get()
driver.maximize_window()
driver.find_element()
driver.find_elements()
send_keys()
click()
driver.back()
driver.refresh()
time.sleep()
driver.quit()
Project Structure
assignment12-Selenium-Getting-Data/
│
├── 1.py
├── Task_1.py
└── README.md
How to Run

Open the project in Visual Studio Code.

Make sure the Selenium environment is selected and Selenium is installed.

Run the program using:

& ".\.selenium_env\Scripts\python.exe" ".\assignment12-Selenium-Getting-Data\1.py"

The Chrome browser will open automatically and perform the required operations.

Execution Flow
Start
  |
  v
Create Chrome WebDriver
  |
  v
Maximize Browser
  |
  v
Open Google
  |
  v
Search "Selenium"
  |
  v
Go Back
  |
  v
Open Amazon
  |
  v
Locate Element using CLASS_NAME
  |
  v
Click Today's Deals using LINK_TEXT
  |
  v
Refresh Page
  |
  v
Search "Gaming Laptop" using XPATH
  |
  v
Extract Product Elements
  |
  v
Display Product Data
  |
  v
Close Browser
  |
  v
End
Expected Output

The program successfully performs Google and Amazon automation and extracts product information from the Amazon search results.

Example output:

Google search completed.
Navigated back to Google.
Amazon opened.
Button clicked using CLASS_NAME.
Today's Deals clicked.
Amazon page refreshed.
Gaming Laptop search completed.


18 items found
------------------------------------------------------------
Item No.1 - KAIGERR 2026 Laptop, 24GB DDR5 512GB SSD Intel Cor
Item No.2 - 2026 Flagship 15.6" Gaming Laptop | AMD Ryzen 7 68
Item No.3 - msi Cyborg 17 17.3" FHD 144Hz Gaming Laptop
Item No.4 - Lenovo Gaming Laptop, Intel Core i7-13620H
Item No.5 - Lenovo Gaming Laptop, AMD 6-core Ryzen 5 7535HS
Item No.6 - msi Katana 15 HX 15.6” 165Hz QHD+ Gaming Laptop
Item No.7 - UPERFECT Delta 18.5" 100Hz Touchscreen
Item No.8 - Lenovo Gaming Laptop, AMD 6-core Ryzen 5 7535HS
Item No.9 - Acer Predator Helios Neo 14 AI Gaming Laptop
Item No.10 - NIMO 15.6" IPS FHD-Light Gaming-Laptop
Item No.11 - KAIGERR Gaming Laptop, 1TB NVMe SSD 16GB RAM
Item No.12 - Newsoul 23.8'' Portable Monitor 144Hz
Item No.13 - KAIGERR Gaming Laptop, Laptops with AMD Ryzen
Item No.14 - Light Gaming Laptop, AMD Ryzen 7 5700U
Item No.15 - KAIGERR 2026 Laptop, 24GB DDR5 512GB SSD
Item No.16 - Lenovo IdeaPad Slim 3i 15.6" FHD Laptop
Item No.17 - Kado 2-Pack 15.6-inch FHD Portable Monitor
Item No.18 - Kado 15.6-Inch 75Hz Portable Monitor
------------------------------------------------------------
Data extraction completed.
Browser closed successfully.
Result

The Selenium WebDriver program successfully automates browser actions on Google and Amazon.

During testing, the program successfully extracted 18 items from the Amazon search results and displayed their information in the console.

The program also successfully demonstrated different Selenium locators including:

By.NAME
By.CLASS_NAME
By.LINK_TEXT
By.XPATH
Conclusion

This assignment demonstrates the basic use of Selenium WebDriver with Python for browser automation and web data extraction. The program performs searching, clicking, navigation, refreshing, locating elements, extracting multiple elements, and displaying extracted data.

Author

Shubham Kumar