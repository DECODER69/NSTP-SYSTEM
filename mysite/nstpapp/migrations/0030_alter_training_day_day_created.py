# Generated by Django 4.0.1 on 2022-09-10 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0029_extenduser_td1_extenduser_td10_extenduser_td11_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training_day',
            name='day_created',
            field=models.DateField(default=''),
        ),
    ]