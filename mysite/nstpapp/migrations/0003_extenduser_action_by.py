# Generated by Django 4.0.1 on 2023-01-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0002_extenduser_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='action_by',
            field=models.CharField(default='', max_length=20),
        ),
    ]