# Generated by Django 4.1.2 on 2022-10-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0020_finals'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='first_equivalents',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='first_merits',
            field=models.CharField(default='100', max_length=20),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='second_equivalents',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='second_merits',
            field=models.CharField(default='100', max_length=20),
        ),
    ]
