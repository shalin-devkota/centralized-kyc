# Generated by Django 4.2.7 on 2024-01-28 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_verifieduser_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='verifieduser',
            old_name='signautre',
            new_name='signature',
        ),
    ]