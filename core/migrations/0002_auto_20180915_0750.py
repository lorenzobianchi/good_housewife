# Generated by Django 2.1.1 on 2018-09-15 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spesa',
            name='data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
