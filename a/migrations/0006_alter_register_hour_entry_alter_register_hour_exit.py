# Generated by Django 4.0.3 on 2022-03-09 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0005_alter_register_hour_entry_alter_register_hour_exit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='hour_entry',
            field=models.TimeField(max_length=26),
        ),
        migrations.AlterField(
            model_name='register',
            name='hour_exit',
            field=models.TimeField(blank=True, default=None, max_length=26, null=True),
        ),
    ]
