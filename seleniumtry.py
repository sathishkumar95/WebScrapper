from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.google.com")

# open a link in a new window
actions = ActionChains(driver)
about = driver.find_element_by_link_text('About')
actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()

driver.switch_to.window(driver.window_handles[-1])
driver.get("https://stackoverflow.com")