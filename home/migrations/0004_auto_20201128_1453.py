# Generated by Django 3.1.3 on 2020-11-28 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201128_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal',
            old_name='mid_name',
            new_name='mid',
        ),
    ]
