# Generated by Django 4.0.2 on 2022-04-14 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_alter_employee_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='irich',
            new_name='business',
        ),
    ]
