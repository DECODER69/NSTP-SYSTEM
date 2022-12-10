# Generated by Django 4.1.2 on 2022-12-10 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpapp', '0007_cwts_certification'),
    ]

    operations = [
        migrations.CreateModel(
            name='cwts_school_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years', models.CharField(blank=True, max_length=20, null=True)),
                ('sem', models.CharField(default='First Term', max_length=20)),
                ('acts', models.CharField(default='PENDING', max_length=20)),
                ('acts_2', models.CharField(default='PENDING', max_length=20)),
                ('date_generated', models.DateTimeField(null=True)),
                ('date_generated_2', models.DateTimeField(null=True)),
                ('commandant', models.CharField(default='', max_length=20)),
                ('registrar', models.CharField(default='', max_length=20)),
                ('month', models.CharField(default='', max_length=20)),
                ('date', models.CharField(default='', max_length=20)),
                ('year', models.CharField(default='', max_length=20)),
                ('status', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
