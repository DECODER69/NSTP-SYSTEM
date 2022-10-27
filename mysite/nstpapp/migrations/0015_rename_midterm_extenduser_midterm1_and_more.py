# Generated by Django 4.1.2 on 2022-10-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0014_alter_midterm_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extenduser',
            old_name='midterm',
            new_name='midterm1',
        ),
        migrations.RenameField(
            model_name='extenduser',
            old_name='midterm_credits',
            new_name='midterm1_credits',
        ),
        migrations.AddField(
            model_name='extenduser',
            name='midterm2',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='extenduser',
            name='midterm2_credits',
            field=models.CharField(default='', max_length=20),
        ),
    ]
