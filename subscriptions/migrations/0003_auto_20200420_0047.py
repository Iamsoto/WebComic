# Generated by Django 3.0.2 on 2020-04-20 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_customemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='customemail',
            name='custom_recipients',
            field=models.CharField(blank=True, help_text="Leave blank if you want to send to everyone in 'Subscriptions'. Seperate with comma", max_length=3000, null=True),
        ),
        migrations.AddField(
            model_name='customemail',
            name='date_sent',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customemail',
            name='send_now',
            field=models.BooleanField(default=True, help_text="If this box is checked, the email will be sent directly after you press 'save'"),
        ),
    ]
