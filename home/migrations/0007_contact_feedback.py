# Generated by Django 3.1 on 2020-10-13 18:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201005_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='feedback',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
