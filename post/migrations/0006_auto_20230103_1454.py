# Generated by Django 3.2.16 on 2023-01-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20221206_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image_filter',
        ),
        migrations.AddField(
            model_name='post',
            name='post_tag',
            field=models.CharField(choices=[('game', 'Game'), ('film', 'Film'), ('boardgame', 'Boardgame'), ('book', 'Book'), ('tv series', 'Tv Series')], default='game', max_length=32),
        ),
    ]