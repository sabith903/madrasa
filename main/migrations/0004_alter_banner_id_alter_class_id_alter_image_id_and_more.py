# Generated by Django 5.1.7 on 2025-03-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_banner_alter_class_id_alter_image_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='class',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID'),
        ),
    ]
