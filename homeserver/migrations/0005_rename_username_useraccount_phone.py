# Generated by Django 5.1.5 on 2025-02-12 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeserver', '0004_remove_homeservertoken_hs_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='username',
            new_name='phone',
        ),
    ]
