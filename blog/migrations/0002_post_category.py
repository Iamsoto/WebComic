# Generated by Django 3.0.2 on 2020-02-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, max_length=144, null=True),
        ),
    ]
