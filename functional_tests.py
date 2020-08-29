from selenium import webdriver
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
        self.fail('Finish the test!')  

        # He proceeds to update his skills section
        
        # He types "xxxxxxxxxxxxx" into a text box (Samuel took
        # this course over the summer)

        # When he hits enter, the page updates, and now the page shows
        # the new updated skills section 

        # There is still a text box inviting him to add another skill. He
        # enters "xxxxxxxxxxxxxxxxxx" and saves

        # The page updates again, and now shows both skills on the updated list

        # Samuel visits the view page to view his cv document

        # Satisfied, he goes back to sleep

        self.browser.quit()

if __name__ == '__main__':  
    unittest.main(warnings='ignore')
