# Generated by Django 4.2.4 on 2023-09-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainApp", "0018_category_remove_flower_color_alter_flower_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=200),
        ),
    ]