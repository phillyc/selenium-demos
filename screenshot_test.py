""" Need to test screenshot capability of selenium """

from selenium import webdriver
import time

# Get local session of Firefox.
browser = webdriver.Firefox()

# Load our page.
browser.get("http://techrangers.cdl.ucf.edu/extended-tech-time-conference/")

time.sleep(1)

print "==== Say cheese! ===="
browser.save_screenshot("screenshots/screenshot_text.png")

browser.close()
