# Generated by Django 4.1.1 on 2022-10-08 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0002_alter_school_year_date_generated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school_year',
            name='acts',
            field=models.CharField(default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='school_year',
            name='date_generated',
            field=models.DateTimeField(default='YYYY-MM-DD', null=True),
        ),
    ]
