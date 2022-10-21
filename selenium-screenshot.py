# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# set chrome driver path
options = Options()
options.chrome_executable_path=r"C:\Users\林楚翔\Desktop\python\chromedriver.exe"

# open chrome
driver = webdriver.Chrome(options=options)
# window maximize
driver.maximize_window()
# open url
driver.get("https://www.google.com/")
driver.save_screenshot("screenshot-google1.png")
# close chrome
driver.close()