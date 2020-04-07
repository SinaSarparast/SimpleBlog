# Generated by Django 3.0.3 on 2020-04-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=400)),
                ('rating', models.IntegerField(null=True)),
                ('lastmodiefied_date', models.DateField(auto_now=True)),
                ('content', models.TextField()),
                ('tags', models.ManyToManyField(null=True, to='articles.Tag')),
            ],
        ),
    ]
