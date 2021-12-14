from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time

class TestProjectBlankPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser=webdriver.Chrome('functional_tests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_dashboard_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(10)

    def test_dashboard_button_redirects_to_blank_page(self):
        self.browser.get(self.live_server_url)

        blank_url=self.live_server_url + reverse('blank')
        self.browser.find_element_by_class_name('dashboard').click()
        self.assertEquals(
            self.browser.current_url,
            blank_url
        )

    def test_user_login_button_redirects_to_login_page(self):
        self.browser.get(self.live_server_url)

        login_url=self.live_server_url + reverse('login')
        button=self.browser.find_element_by_class_name('loginU').click()
        self.assertEquals(
            self.browser.current_url,
            login_url
        )

    def test_admin_login_button_redirects_to_login_page(self):
        self.browser.get(self.live_server_url)

        login_url=self.live_server_url + reverse('login')
        button=self.browser.find_element_by_class_name('loginA').click()
        self.assertEquals(
            self.browser.current_url,
            login_url
        )

    def test_help_button_redirects_to_help_page(self):
        self.browser.get(self.live_server_url)

        help_url=self.live_server_url + reverse('help')
        self.browser.find_element_by_class_name('help').click()
        self.assertEquals(
            self.browser.current_url,
            help_url
        )


        

    
