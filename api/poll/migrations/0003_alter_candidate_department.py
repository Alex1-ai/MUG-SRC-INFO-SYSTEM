# Generated by Django 4.2.4 on 2023-09-06 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_remove_vote_user_vote_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='department',
            field=models.CharField(max_length=17),
        ),
    ]
