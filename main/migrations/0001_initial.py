# Generated by Django 5.1.7 on 2025-03-09 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Classes',
                'unique_together': {('name', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('roll_number', models.CharField(max_length=20)),
                ('reg_number', models.CharField(max_length=100, unique=True)),
                ('class_enrolled', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='main.class')),
            ],
            options={
                'unique_together': {('roll_number', 'class_enrolled')},
            },
        ),
    ]
