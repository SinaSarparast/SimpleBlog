# Generated by Django 3.0.3 on 2020-04-27 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20200413_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(help_text='summary of article', max_length=400),
        ),
    ]
