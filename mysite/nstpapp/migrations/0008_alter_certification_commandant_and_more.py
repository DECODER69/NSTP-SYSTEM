# Generated by Django 4.1.1 on 2022-09-24 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0007_certification_school_year2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='commandant',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='certification',
            name='registrar',
            field=models.CharField(default='', max_length=40),
        ),
    ]
