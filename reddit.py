from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

user_to_upvote = "c_ross"

browser = webdriver.Firefox()  # Get local session of Firefox
browser.get("http://www.reddit.com/u/%s" % user_to_upvote)  # Load page
assert "overview for %s" % user_to_upvote in browser.title  # Sanity check
print "**** %s gets all the upvotes! ****" % user_to_upvote

# Going to find each element of our login form and type our info in.
username = browser.find_element_by_name("user")  # Find the username box
username.send_keys("ehtgutyjdeut29143")  # Send our username
password = browser.find_element_by_name("passwd")  # Find the password box
password.send_keys("password")  # Send our super-secure password

# Using XPath to find our element because it is unnamed.
login = browser.find_element_by_xpath("//*[@id='login_login-main']/div[3]/button")
login.click()
time.sleep(5)  # Let the page load
print "Logged in!"

first_page = True

def click_upvotes(first_page):
  '''
		We need to setup a counter for upvotes.
		A little research shows that reddit only displays 24 comments per page.
		Reddit uses the xpath structure /div[1]/div[1]/div[1]
		Where the first comment starts at div[1] and increments by 2,
		and the last div[1] is 1 for upvote 2 for downvote.
	'''
	counter = 1
	# Loop through each available upvote button
	while counter < 50:
		upvote = browser.find_element_by_xpath("//*[@id='siteTable']/div[%s]/div[1]/div[1]" % counter)
		# And click it!
		upvote.click()
		counter = counter + 2
		print "clicked an upvote button"

	# When we're done clicking on every upvote we need to get the next page.
	next_page(first_page)


def next_page(first_page):
	# We need to know if this is the first page of comments.
	if first_page is True:
		next = browser.find_element_by_xpath("/html/body/div[3]/p/a")
		first_page = False
		print "**** End of first page ****"
	else:
		# Subsequent pages means 'Next' link is the second <a> in the <div>
		next = browser.find_element_by_xpath("/html/body/div[3]/p/a[2]")
	next.click()
	print "Clicked next."
	print "--------------------------"
	print "Running the upvote function again:"
	click_upvotes(first_page)

# This is the main try/except
try:
	click_upvotes(first_page)

except NoSuchElementException:
	assert 0, "Ran out of things to click on. :("
	browser.close()

# Close the browser window.
#browser.close()
print "All done."
