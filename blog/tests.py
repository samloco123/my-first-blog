from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.views import *

class CVPageTest(TestCase):

    def test_url_resolves_to_cv_page_view(self):
        found = resolve('/cv/edit/')  
        self.assertEqual(found.func, cv_edit)

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()  
        response = cv_edit(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('\n<html>'))  
        self.assertIn('<title>CV page</title>', html)  
        self.assertTrue(html.endswith('</html>'))