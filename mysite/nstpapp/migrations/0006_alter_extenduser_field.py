# Generated by Django 4.0.1 on 2022-08-02 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0005_alter_extenduser_idpic_alter_extenduser_proof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='field',
            field=models.CharField(default='', max_length=100),
        ),
    ]