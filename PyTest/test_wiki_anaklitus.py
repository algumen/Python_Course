from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from time import gmtime, strftime
import pytest


class TestWikiAnaklitus():
    def test_open_image_anaklitus(self):
        pass
        print('*********************************************************')
        print(datetime.now())
        wiki_page = webdriver.Chrome()
        wiki_page.get('https://uk.wikipedia.org')
        #assert 'Вікіпедія' in wiki_page.title

        wiki_page.find_element_by_id('searchInput').send_keys('список римських пап')
        wiki_page.find_element_by_id('searchButton').click()
        wiki_page.find_element_by_css_selector("[alt='3-St.Cletus.jpg']").click()

        print(wiki_page.find_element_by_css_selector(r"[href='https://en.wikipedia.org/wiki/Pope_Cletus']"))

        #assert 'Cletus' in wiki_page.find_element_by_css_selector(r"[href='https://en.wikipedia.org/wiki/Pope_Cletus']")
        #print(wiki_page.find_element_by_css_selector(r"[href='https://en.wikipedia.org/wiki/Pope_Cletus']"))
        #print('hjkh')
'''
        search_field = c
        search_field.send_keys('список римських пап')
        search_button =wiki_page.find_element_by_id('searchButton').click()
        search_image = wiki_page.find_element_by_css_selector("[alt='3-St.Cletus.jpg']").click()
'''
