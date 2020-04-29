import unittest

from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class BasicHomePageTest(FunctionalTest):

    def test_can_go_to_page_and_view_users(self):
        self.browser.get(self.server_url)

        # Notice the page title and header text
        self.assertIn('{{ cookiecutter.project_name }}', self.browser.title)
