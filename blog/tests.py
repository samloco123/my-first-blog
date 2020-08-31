from blog.models import Skill
from django.test import TestCase

class CVPageTest(TestCase):

    def test_uses_cv_edit_template(self):
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/cv/edit/', data={'skill_text': 'A new skill'})
        self.assertIn('A new skill', response.content.decode())
        self.assertTemplateUsed(response, 'blog/cv_edit.html')

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
