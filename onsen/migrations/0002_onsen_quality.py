# Generated by Django 3.0.4 on 2021-01-01 11:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('onsen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='onsen',
            name='quality',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
