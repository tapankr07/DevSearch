# Generated by Django 4.1.7 on 2023-04-20 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
