from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Path to Brave browser
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"  # Adjust this path as needed

chromedriver_path = "C:/Users/nedre/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"

# Set up Selenium WebDriver for Brave
chrome_options = Options()
chrome_options.binary_location = brave_path
chrome_options.add_argument("--headless")  # Run in headless mode (no browser window)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
service = Service(chromedriver_path)  # Replace with the path to your ChromeDriver executable

driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the URL
url = "https://shopee.ph/search?keyword=recycled"
driver.get(url)

# Wait for the page to load completely
driver.implicitly_wait(10)

# Get the fully rendered HTML
html = driver.page_source

# Close the browser
driver.quit()

# Parse the HTML with BeautifulSoup
doc = BeautifulSoup(html, "html.parser")

# Search for the peso sign (₱) in the rendered page
prices = doc.find_all(string="₱")
if prices:
    parent = prices[0].parent
    print(parent)
else:
    print("No price found.")
