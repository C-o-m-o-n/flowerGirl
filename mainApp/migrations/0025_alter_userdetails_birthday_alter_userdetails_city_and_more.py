# Generated by Django 4.2.4 on 2023-09-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainApp", "0024_alter_userdetails_birthday_alter_userdetails_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdetails",
            name="birthday",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="userdetails",
            name="city",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="userdetails",
            name="country",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="userdetails",
            name="gender",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="userdetails",
            name="occupation",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="userdetails",
            name="phone",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="userdetails",
            name="street",
            field=models.CharField(max_length=200),
        ),
    ]
