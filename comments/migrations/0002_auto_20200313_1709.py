# Generated by Django 3.0.2 on 2020-03-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-updated_on', '-created_on')},
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
