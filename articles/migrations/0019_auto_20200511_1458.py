# Generated by Django 3.0.3 on 2020-05-11 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20200505_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=500, primary_key=True, serialize=False, unique=True),
        ),
    ]
