# Generated by Django 4.0.1 on 2022-08-18 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0017_extenduser_s_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='s_year',
            field=models.CharField(default='0000', max_length=100),
        ),
    ]