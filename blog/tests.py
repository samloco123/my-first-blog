from blog.models import Skill
from django.test import TestCase

class CVPageTest(TestCase):

    def test_uses_cv_edit_template(self):
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/cv/edit/', data={'skill_text': 'A new skill'})

        self.assertEqual(Skill.objects.count(), 1)
        new_skill = Skill.objects.first()
        self.assertEqual(new_skill.text, 'A new skill')

    def test_redirects_after_POST(self):
        response = self.client.post('/cv/edit/', data={'skill_text': 'A new skill'})

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/edit/')
    
    def test_only_saves_items_when_necessary(self):
        self.client.get('/cv/edit/')
        self.assertEqual(Skill.objects.count(), 0)

    def test_displays_all_skills(self):
        Skill.objects.create(text='skilley 1')
        Skill.objects.create(text='skilley 2')

        response = self.client.get('/cv/edit/')

        self.assertIn('skilley 1', response.content.decode())
        self.assertIn('skilley 2', response.content.decode())

class SkillModelTest(TestCase):

    def test_saving_and_retrieving_skills(self):
        first_skill = Skill()
        first_skill.text = 'The first (ever) skill'
        first_skill.save()

        second_skill = Skill()
        second_skill.text = 'Skill the second'
        second_skill.save()

        saved_skills = Skill.objects.all()
        self.assertEqual(saved_skills.count(), 2)

        first_saved_skill = saved_skills[0]
        second_saved_skill = saved_skills[1]
        self.assertEqual(first_saved_skill.text, 'The first (ever) skill')
        self.assertEqual(second_saved_skill.text, 'Skill the second')
