from django.test import TestCase

class CVPageTest(TestCase):

    def test_uses_cv_edit_template(self):
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

  