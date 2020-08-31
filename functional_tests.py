from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def check_for_skill_in_skill_list(self, skl_text):
        slist = self.browser.find_element_by_id('id_skill_list')
        skls = slist.find_elements_by_tag_name('li')
        self.assertIn(skl_text, [skl.text for skl in skls])

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
        inputbox = self.browser.find_element_by_id('id_new_skill')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter new skill'
        )

        # He types "Intermidiate Java programmer" into a text box 
        inputbox.send_keys('Intermidiate Java programmer')

        # When he hits enter, the page updates, and now the page shows
        # the new updated skills section
        inputbox.send_keys(Keys.ENTER)  
        time.sleep(1)
        self.check_for_skill_in_skill_list('Intermidiate Java programmer')
        
        # There is still a text box inviting him to add another skill. He
        # enters "Foreign languages" and saves

        inputbox = self.browser.find_element_by_id('id_new_skill')
        inputbox.send_keys('Foreign languages')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both skills on the updated list
        self.check_for_skill_in_skill_list('Intermidiate Java programmer')
        self.check_for_skill_in_skill_list('Foreign languages')

        # Samuel visits the view page to view his cv document
        self.fail('Finish the test!')

        # Satisfied, he goes back to sleep

        self.browser.quit()

if __name__ == '__main__':  
    unittest.main(warnings='ignore')
