from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()


    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000/chatbot')
        self.assertIn("Hi! I'm a bot. What's up?", self.browser.page_source)
    
    def test_of_hello(self):
        self.browser.get('http://localhost:8000/chatbot')
        text = self.browser.find_element_by_id('user-input')
        text.send_keys('hello')
        self.browser.find_element_by_id('user-input').send_keys(Keys.ENTER)
        time.sleep(20)
        text = self.browser.find_element_by_id('user-message').text
        self.assertIn(text, self.browser.page_source)
    
    def tearDown(self):
        self.browser.quit()

class UnitTestCase(TestCase):

    def test_chatbot_template(self):
        response = self.client.get('/chatbot/')
        self.assertTemplateUsed(response, 'home.html')
    