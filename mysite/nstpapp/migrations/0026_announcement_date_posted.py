# Generated by Django 4.0.1 on 2022-09-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0025_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='date_posted',
            field=models.CharField(default='', max_length=500),
        ),
    ]