# Generated by Django 3.0.3 on 2020-04-10 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20200410_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='slug'),
        ),
    ]