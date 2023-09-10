from django.db import migrations
from api.account.models import User


class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user = User(
            username="Alex",
            email="alexanderemmanuel1719@gmail.com",
            is_staff=True,
            is_superuser=True,
            # contact='0238559158',
            # gender='Male'
        )
        user.set_password('123123')
        user.save()


    
    dependencies= [

    ]

    operations= [
        migrations.RunPython(seed_data),
    ]