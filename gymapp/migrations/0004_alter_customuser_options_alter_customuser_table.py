# Generated by Django 5.1.6 on 2025-04-05 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0003_routine_routine_type_trainingsession'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='gymapp_customuser',
        ),
    ]
