# Generated by Django 3.0.3 on 2020-07-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20200511_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(max_length=2200),
        ),
    ]