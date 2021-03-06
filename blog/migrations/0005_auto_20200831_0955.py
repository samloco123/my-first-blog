# Generated by Django 2.2.12 on 2020-08-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=200)),
                ('qualif', models.CharField(max_length=50)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('dating', models.CharField(max_length=50)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
