# Generated by Django 4.2.6 on 2023-10-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0010_alter_submissions_usersubmision'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='contestType',
            field=models.CharField(choices=[('typing', 'typing'), ('mcq', 'mcq')], default='mcq', max_length=20),
        ),
    ]
