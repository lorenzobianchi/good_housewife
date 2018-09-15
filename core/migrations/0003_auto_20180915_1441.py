# Generated by Django 2.1.1 on 2018-09-15 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180915_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSpesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='spesa',
            name='spesa_ordinaria',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='spesa',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TipoSpesa'),
        ),
    ]
