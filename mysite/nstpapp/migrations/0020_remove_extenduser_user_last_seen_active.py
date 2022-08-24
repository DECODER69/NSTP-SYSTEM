# Generated by Django 4.0.1 on 2022-08-24 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nstpapp', '0019_extenduser_user_last_seen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extenduser',
            name='user_last_seen',
        ),
        migrations.CreateModel(
            name='Active',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_last_seen', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]