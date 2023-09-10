# Generated by Django 4.2.4 on 2023-09-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.AddField(
            model_name='vote',
            name='email',
            field=models.EmailField(default='alex@gmail.com', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]