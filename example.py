# This is our webdriver.
from selenium import webdriver

# This lets us snooze.
import time

# Get local session of Firefox.
browser = webdriver.Firefox()

# Load our page.
browser.get("http://techrangers.cdl.ucf.edu/extended-tech-time-conference/")

# Sanity check.
assert "Extended Tech Time Conference" in browser.title

print "Our homepage works!"
time.sleep(5)

# Find the poster image with XPath
poster = browser.find_element_by_xpath("//*[@id='content']/div/p[5]/a/img")
print "Navigating to the poster using XPath."

# Click the poster
poster.click()

# Wait for the page to load
time.sleep(5)

# Another sainty check
assert "2013_06_11_TT_Flyer_Extended_TechTime.png" in browser.title

print "It's all good in the hood!"
time.sleep(10)

# Close the browser
browser.close()
