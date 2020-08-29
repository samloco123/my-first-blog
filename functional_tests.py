from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Samuel opens the edit cv page on his  website so he can update
        # parts of it as he's gained more experience/skills
        self.browser.get('http://localhost:8000/cv/edit')

        # Checks if the title and header mention CV 
        # like they should
        self.assertIn('CV page', self.browser.title)  
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('My CV', header_text)  

        # He proceeds to update his skills section
        inputbox = self.browser.find_element_by_id('id_new_item')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter experience/new skill'
        )

        # He types "Intermidiate Java programmer" into a text box 
        inputbox.send_keys('Intermidiate Java programmer')

        # When he hits enter, the page updates, and now the page shows
        # the new updated skills section
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == 'Intermidiate Java programmer' for row in rows)
        )

        # There is still a text box inviting him to add another skill. He
        # enters "xxxxxxxxxxxxxxxxxx" and saves
        self.fail('Finish the test!')

        # The page updates again, and now shows both skills on the updated list

        # Samuel visits the view page to view his cv document

        # Satisfied, he goes back to sleep

        self.browser.quit()

if __name__ == '__main__':  
    unittest.main(warnings='ignore')
