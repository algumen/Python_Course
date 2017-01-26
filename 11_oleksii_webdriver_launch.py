from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_page = webdriver.Chrome()
chrome_page.get('https://uk.wikipedia.org/')
chrome_page.maximize_window()
search_field = chrome_page.find_element_by_id('searchInput')
search_field.send_keys('список римських пап')
search_button =chrome_page.find_element_by_id('searchButton').click()
search_image = chrome_page.find_element_by_css_selector("[alt='3-St.Cletus.jpg']").click()
