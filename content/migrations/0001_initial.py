# Generated by Django 3.0.2 on 2020-03-18 22:06

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=144)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField()),
                ('position', models.IntegerField(help_text='Where your content is ordered in the nav bar')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
