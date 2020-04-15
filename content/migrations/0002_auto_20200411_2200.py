# Generated by Django 3.0.2 on 2020-04-11 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='position',
            field=models.IntegerField(blank=True, help_text='Where your content is ordered in the nav bar', null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=144, unique=True),
        ),
    ]