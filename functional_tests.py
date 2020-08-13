from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_add_a_post_and_retrieve_it_later(self):  
        # Sam's has heard about a cool new online blog page. He goes
        # to check out its homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention django girls
        self.assertIn('Django Girls', self.browser.title)  
        self.fail('Finish the test!')  

        # He is invited to enter a to-do item straight away
        # He is invited to enter a blog post straight away

        # He types ++"Buy peacock feathers" into a text box (Sam's hobby
        # is tying fly-fishing lures)++

        # When he hits enter, the page updates, and now the page ++lists
        # "1: Buy peacock feathers" as an item in a to-do list++

        # There is still a text box inviting him to add another post. He
        # enters ++"Use peacock feathers to make a fly" (Sam is very methodical)++

        # The page updates again, and now shows both posts on the blog

        # +++Sam wonders whether the site will remember his list. Then he sees
        # that the site has generated a unique URL for him -- there is some
        # explanatory text to that effect.+++

        # +++He visits that URL - his to-do list is still there.+++

        # Satisfied, he goes back to sleep

if __name__ == '__main__':  
    unittest.main(warnings='ignore')