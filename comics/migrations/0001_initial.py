# Generated by Django 3.0.2 on 2020-02-20 18:53

import ckeditor_uploader.fields
import comics.models
from django.db import migrations, models
import django.db.models.deletion
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
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('caption', models.CharField(max_length=500)),
                ('series', models.CharField(default=comics.models.getMainSeriesName, help_text='The default value is what the main Series Name is set to in Settings.py', max_length=255)),
                ('chapter', models.FloatField(blank=True, null=True)),
                ('episode', models.IntegerField(blank=True, null=True)),
                ('uploadTime', models.DateField(default=django.utils.timezone.now)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='comics/thumbnails/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=144, null=True)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('ComicPanel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='comics.ComicPanel')),
            ],
        ),
        migrations.AddConstraint(
            model_name='comicpanel',
            constraint=models.UniqueConstraint(fields=('series', 'chapter', 'episode'), name='Must be null or unique'),
        ),
    ]
