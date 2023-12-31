# Generated by Django 4.2.3 on 2023-09-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teas', '0006_rename_tea_id_teacharacteristics_tea_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='tea_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='tea',
            name='tea_type',
            field=models.CharField(choices=[('GREEN', 'GREEN'), ('WHITE', 'WHITE'), ('BLACK', 'BLACK'), ('RED', 'RED'), ('YERBA', 'YERBA'), ('MATCHA', 'MATCHA')], max_length=10),
        ),
    ]
