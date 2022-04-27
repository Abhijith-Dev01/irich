# Generated by Django 4.0.2 on 2022-04-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_employee_is_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='is_user',
        ),
        migrations.AddField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
