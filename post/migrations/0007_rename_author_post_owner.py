# Generated by Django 3.2.4 on 2023-03-30 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20230103_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='owner',
        ),
    ]