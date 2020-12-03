# Generated by Django 3.1.3 on 2020-11-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201127_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_num', models.CharField(blank=True, max_length=50)),
                ('premise_name', models.CharField(blank=True, max_length=50)),
                ('road_name', models.CharField(blank=True, max_length=50)),
                ('pincode', models.CharField(blank=True, max_length=50)),
                ('area', models.CharField(blank=True, max_length=50)),
                ('town_name', models.CharField(blank=True, max_length=50)),
                ('state_name', models.CharField(blank=True, max_length=50)),
                ('country_name', models.CharField(blank=True, max_length=50)),
                ('contact_number', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('email2', models.EmailField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=50)),
                ('dob', models.DateField()),
                ('pan_number', models.CharField(blank=True, max_length=50)),
                ('father_name', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('marital_status', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(blank=True, max_length=50)),
                ('employer_type', models.CharField(blank=True, max_length=50)),
                ('salary', models.CharField(blank=True, max_length=50)),
                ('perquisites', models.CharField(blank=True, max_length=50)),
                ('profit', models.CharField(blank=True, max_length=50)),
                ('allowances', models.CharField(blank=True, max_length=50)),
                ('balance', models.CharField(blank=True, max_length=50)),
                ('deduction', models.CharField(blank=True, max_length=50)),
                ('std_deduciton', models.CharField(blank=True, max_length=50)),
                ('professional_tax', models.CharField(blank=True, max_length=50)),
                ('income_chargeable', models.CharField(blank=True, max_length=50)),
                ('tds', models.CharField(blank=True, max_length=50)),
                ('tan', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Data',
        ),
    ]
