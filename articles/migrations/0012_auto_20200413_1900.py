# Generated by Django 3.0.3 on 2020-04-13 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20200410_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
    ]