# Generated by Django 4.2.6 on 2023-10-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0013_submissions_backspacecount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissions',
            name='wordsPerMin',
        ),
        migrations.AddField(
            model_name='submissions',
            name='accuracy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submissions',
            name='correctWords',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submissions',
            name='gwpm',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submissions',
            name='incorrectWords',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submissions',
            name='nwpm',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='submissions',
            name='totalWords',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='subTime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
