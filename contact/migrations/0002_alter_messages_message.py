# Generated by Django 4.2.3 on 2023-10-22 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
    ]
