# Generated by Django 4.1.3 on 2022-11-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurante", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itempedido",
            name="hr_entregue",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="itempedido",
            name="hr_pedido",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]