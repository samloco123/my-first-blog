from django.urls import resolve
from django.test import TestCase
from blog.views import *

class CVPageTest(TestCase):

    def test_url_resolves_to_cve_page_view(self):
        found = resolve('/cv/edit/')  
        self.assertEqual(found.func, cv_edit)
