# Generated by Django 5.0.4 on 2024-05-02 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_game_author_alter_game_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='published_date',
            field=models.DateField(),
        ),
    ]