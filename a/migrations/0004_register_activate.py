# Generated by Django 4.0.3 on 2022-03-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0003_alter_register_hour_exit_alter_register_totals'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='activate',
            field=models.BooleanField(default=True),
        ),
    ]
