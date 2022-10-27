# Generated by Django 4.1.2 on 2022-10-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0015_rename_midterm_extenduser_midterm1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extenduser',
            old_name='finals',
            new_name='finals1',
        ),
        migrations.RenameField(
            model_name='extenduser',
            old_name='finals_credits',
            new_name='finals2',
        ),
        migrations.AddField(
            model_name='extenduser',
            name='finals_credits1',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='finals_credits2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='first_sem',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='second_sem',
            field=models.CharField(default='', max_length=20),
        ),
    ]