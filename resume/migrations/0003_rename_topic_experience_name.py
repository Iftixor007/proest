# Generated by Django 4.2.3 on 2023-07-18 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='topic',
            new_name='name',
        ),
    ]