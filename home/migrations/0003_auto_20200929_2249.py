# Generated by Django 3.1 on 2020-09-29 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200929_2243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditem',
            old_name='Item',
            new_name='Item_name',
        ),
    ]