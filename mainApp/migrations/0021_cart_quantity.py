# Generated by Django 4.2.4 on 2023-09-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainApp", "0020_rename_item_category_orders_adress_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]