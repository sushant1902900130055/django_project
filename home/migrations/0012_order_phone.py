# Generated by Django 3.1 on 2020-10-14 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20201015_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
