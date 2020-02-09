# Generated by Django 3.0.2 on 2020-02-07 00:18

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComicPanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='comics/')),
                ('description', ckeditor.fields.RichTextField()),
                ('caption', models.CharField(max_length=500)),
                ('series', models.CharField(max_length=255)),
                ('chapter', models.FloatField(blank=True, null=True)),
                ('episode', models.IntegerField(blank=True, null=True)),
                ('uploadTime', models.DateField(default=django.utils.timezone.now)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='comics/thumbnails/')),
            ],
        ),
        migrations.AddConstraint(
            model_name='comicpanel',
            constraint=models.UniqueConstraint(fields=('series', 'chapter', 'episode'), name='Must be null or unique'),
        ),
    ]