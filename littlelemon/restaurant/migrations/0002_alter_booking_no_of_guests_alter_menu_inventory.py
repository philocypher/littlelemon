# Generated by Django 4.2.5 on 2023-09-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(),
        ),
    ]