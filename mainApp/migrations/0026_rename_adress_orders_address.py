# Generated by Django 4.2.4 on 2023-09-27 08:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainApp", "0025_alter_userdetails_birthday_alter_userdetails_city_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orders",
            old_name="adress",
            new_name="address",
        ),
    ]
