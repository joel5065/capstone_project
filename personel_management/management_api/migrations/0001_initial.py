# Generated by Django 5.1.7 on 2025-03-19 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Military',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=200)),
                ('rank', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('departement', models.CharField(max_length=50)),
                ('registration_number', models.IntegerField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='pofile_pictures/')),
                ('sex', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=1)),
                ('is_maried', models.CharField(choices=[('M', 'MARIED'), ('S', 'SINGLE'), ('D', 'DIVORCED')], max_length=1)),
                ('graduation_school', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diploma_title', models.CharField(max_length=100)),
                ('type_of_diploma', models.CharField(choices=[('M', 'Military'), ('C', 'Civilian')], max_length=1)),
                ('date_of_production', models.DateField()),
                ('school_of_graduation', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_api.military')),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_api.military')),
            ],
        ),
    ]
