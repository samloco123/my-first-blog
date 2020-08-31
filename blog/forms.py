from django import forms

from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'thumb')

class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ('text',)

class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ( 'job_title', 'time_frame','text')

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ( 'school', 'qualification','text')