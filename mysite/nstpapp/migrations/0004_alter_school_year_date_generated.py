# Generated by Django 4.1.1 on 2022-10-08 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0003_alter_school_year_acts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_year',
            name='date_generated',
            field=models.DateTimeField(null=True),
        ),
    ]
