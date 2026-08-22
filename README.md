# Assignment 12 – Selenium Web Automation & Data Extraction

## 📌 Project Overview

This project demonstrates web automation and data extraction using **Python Selenium WebDriver**.

The program automates browser activities such as opening websites, performing Google searches, navigating between pages, opening Amazon, searching for a product using XPath, and extracting product information from the search results.

This assignment was developed as part of the **Tutedude Python Programming course**.

---

## 🎯 Objectives

The main objectives of this project are:

* Automate web browsers using Selenium WebDriver.
* Open and navigate between different web pages.
* Perform Google search automation.
* Navigate back to previously visited pages.
* Open Amazon using Selenium.
* Locate web elements using XPath.
* Search for "Gaming Laptop" on Amazon.
* Extract product names from search results.
* Display extracted data in the terminal.
* Capture screenshots of important automation steps.

---

## 🛠️ Technologies Used

* **Python**
* **Selenium WebDriver**
* **Chrome Browser**
* **ChromeDriver / Selenium Manager**
* **XPath**
* **Git & GitHub**

---

## 📂 Project Structure

```text
assignment12-Selenium-Getting-Data/
│
├── Getting_data.py
│
├── Screen_Shot/
│   ├── Amazon_Navigation.png
│   ├── Console_output-Extract_Data.png
│   ├── Google_Search_Automation.png
│   └── Product_Search_Result.png
│
└── readme.md
```

---

## ⚙️ Requirements

Make sure Python is installed on your system.

Install Selenium using:

```bash
pip install selenium
```

Check the installation:

```bash
python -c "import selenium; print(selenium.__version__)"
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Hydraneo0/assignment12-Selenium-Getting-Data.git
```

### 2. Open the project folder

```bash
cd assignment12-Selenium-Getting-Data
```

### 3. Install dependencies

```bash
pip install selenium
```

### 4. Run the Python script

```bash
python Getting_data.py
```

The Chrome browser will open automatically and Selenium will perform the defined automation tasks.

---

## 🔎 Automation Tasks Performed

### 1. Google Search

The script opens Google and performs an automated search.

```text
Google → Search → Search Results
```

---

### 2. Navigate Back

After completing the Google search, Selenium navigates back to the previous page using:

```python
driver.back()
```

---

### 3. Open Amazon

The script then opens Amazon:

```python
driver.get("https://www.amazon.com")
```

---

### 4. Search for Gaming Laptop

The Amazon search box is located using XPath and the search term is entered:

```python
search.send_keys("Gaming Laptop")
```

---

### 5. XPath-Based Interaction

XPath is used to locate web elements.

Example:

```python
By.XPATH
```

This demonstrates how Selenium can interact with specific elements on a webpage.

---

### 6. Product Data Extraction

After searching for the product, the script extracts product names from the search results and displays them in the terminal.

Example output:

```text
Item No.6 - MSI Katana 15 HX 15.6" 165Hz QHD+ Gaming Laptop
Item No.7 - ASUS V16 16" WUXGA 144Hz Gaming Laptop
Item No.8 - 2026 AMD Gaming Laptop with Ryzen Processor
Item No.9 - Laptop, 2026 New Laptop Computer
...
```

---

## 📸 Screenshots

The `Screen_Shot` folder contains screenshots demonstrating:

* Google search automation
* Amazon navigation
* Product search results
* Extracted data displayed in the console

---

## 💻 Expected Output

When the script runs successfully:

1. Chrome browser opens.
2. Google is opened.
3. A search is performed.
4. Browser navigation is performed.
5. Amazon is opened.
6. "Gaming Laptop" is searched.
7. Product information is extracted.
8. Extracted products are displayed in the terminal.
9. Data extraction is completed.
10. Browser closes successfully.

Example:

```text
Google search completed.
Navigated back to Google.

Item No.6 - MSI Katana 15 HX...
Item No.7 - ASUS V16...
Item No.8 - AMD Gaming Laptop...
Item No.9 - Laptop...
...

Data extraction completed.
Browser closed successfully.
```

---

## 🧠 Key Concepts Learned

Through this project, the following Selenium concepts were practiced:

* WebDriver initialization
* Browser navigation
* `driver.get()`
* `driver.back()`
* `time.sleep()`
* Finding elements
* XPath selectors
* `send_keys()`
* Clicking web elements
* Web data extraction
* Browser automation
* Handling dynamic web pages
* Saving screenshots
* Closing WebDriver

---

## ⚠️ Important Note

Websites such as Amazon and Google can change their HTML structure, element IDs, XPath selectors, or page layout.

Therefore, XPath selectors used in this project may need to be updated if the website structure changes.

This project is intended for **educational and automation-learning purposes**.

---

## 👨‍💻 Author

**Shubham Kumar**

GitHub:
https://github.com/Hydraneo0

---

## 📚 Course

**Tutedude – Python Programming Course**

**Assignment:** Assignment 12 – Selenium Web Automation & Data Extraction
