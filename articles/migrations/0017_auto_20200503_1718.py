# Generated by Django 3.0.3 on 2020-05-03 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20200429_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(help_text='summary of article', max_length=2200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
