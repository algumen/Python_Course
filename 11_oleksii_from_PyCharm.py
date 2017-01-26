from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

chrome_page = webdriver.Chrome()
chrome_page.get('https://uk.wikipedia.org/')
chrome_page.maximize_window()
search_field = chrome_page.find_element_by_id('searchInput')
search_field.send_keys('список римських пап')
search_button =chrome_page.find_element_by_id('searchButton').click()
search_image = chrome_page.find_element_by_css_selector("[alt='3-St.Cletus.jpg']").click()

'''
#chrome_page.assertTrue(chrome_page.is_text_present("Анакліт"))
#chrome_page.assertTrue(chrome_page.is_element_present(By.LINK_TEXT, "My link"))

try:
    chrome_page.find_element_by_xpath(xpath)
except NoSuchElementException:
    return False
return True
'''