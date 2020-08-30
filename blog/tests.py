from django.test import TestCase

class CVPageTest(TestCase):

    def test_uses_cv_edit_template(self):
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/cv/edit/', data={'skill_text': 'A new skill'})
        self.assertIn('A new skill', response.content.decode())
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

  