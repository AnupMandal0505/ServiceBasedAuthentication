# Generated by Django 5.1.5 on 2025-02-12 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeserver', '0003_homeservertoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeservertoken',
            name='hs_user',
        ),
        migrations.AlterField(
            model_name='homeservertoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='auth_token', to='homeserver.homeserver'),
        ),
    ]
