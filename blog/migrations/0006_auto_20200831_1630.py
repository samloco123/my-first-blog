# Generated by Django 2.2.12 on 2020-08-31 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200831_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='text',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_text',
            field=models.TextField(default=''),
        ),
    ]