# Generated by Django 3.2.9 on 2022-03-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_answers_true_or_false'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='answer',
        ),
        migrations.AddField(
            model_name='registration',
            name='answer',
            field=models.ManyToManyField(to='main.Answers'),
        ),
    ]
