# Generated by Django 3.1.4 on 2020-12-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_documentupload'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentupload',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]