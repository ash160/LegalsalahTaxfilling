# Generated by Django 3.1.4 on 2020-12-03 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20201202_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='doc/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]