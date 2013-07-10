from selenium import webdriver
import time


# Define our root url
root_url = "http://techrangers.cdl.ucf.edu/"

# Get local session of Firefox.
browser = webdriver.Firefox()


print "---- Opening page..."
browser.get(root_url)
print "==== Taking a screenshot of the homepage. Say cheese! ===="
browser.save_screenshot("screenshots/home.png")


def build_link_list(root_url):
  """
		build_link_list is passed root_url, which is defined as the homepage of our target site.
		This function will traverse the DOM of root_url, looking for links, then refining the list of
		links to only those that are children of root_url, which it returns as children_links.
	"""
	print "---- Getting all links..."
	all_links = browser.find_elements_by_tag_name("a")

	# Need to transform all_links to a list of strings, not elements.
	as_text_all_links = []
	for link in all_links:
		as_text_all_links.append(link.get_attribute("href"))

	# Now that we have a list of strings, we can see if they start with our root_url.
	if len(all_links) is not 0:
		print "---- Filtering for internal links:"

		# Long form way of doing this.
		# for link in as_text_all_links:
		# 	if link.startswith(root_url):
		# 		internal_links.append(link)

		# Using a list comprehension to store any link that starts with root_url to list.
		internal_links = [link for link in as_text_all_links if link.startswith(root_url)]

		if internal_links == []:
			print "xxxx There are no internal links on this page! xxxx"
			return False

		print "---- Dropping any duplicate links..."
		set_of_internal_links = set(internal_links)

		print "---- Disregarding self-referential links..."
		child_links = []
		for link in set_of_internal_links:
			if link != root_url and link != root_url + "#":
				child_links.append(link)
		return child_links

	else:
		print "xxxx Didn't find any links on this page! xxxx"
		return False


def take_screenshots(root_url):
	child_links = build_link_list(root_url)

	for link in child_links:
		print "///// Navigating to child link %s" % link
		browser.get(link)
		time.sleep(2)
		try:
			# This is really all you need to do to take a screenshot.
			print "===== Say cheese! ======"
			browser.save_screenshot('screenshots/screenshot_%s.png' % time.time())
		except:
			print "Something broke. :/"


take_screenshots(root_url)
browser.close()
