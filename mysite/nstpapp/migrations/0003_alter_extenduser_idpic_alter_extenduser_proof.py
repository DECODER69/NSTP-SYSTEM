# Generated by Django 4.0.1 on 2022-08-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0002_alter_extenduser_idpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='idpic',
            field=models.ImageField(default='', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='extenduser',
            name='proof',
            field=models.FileField(default='', null=True, upload_to='proofs/'),
        ),
    ]