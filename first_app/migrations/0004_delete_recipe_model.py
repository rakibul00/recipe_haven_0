# Generated by Django 5.1.3 on 2024-11-13 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_recipe_model'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe_model',
        ),
    ]