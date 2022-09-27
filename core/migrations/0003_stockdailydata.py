# Generated by Django 4.1 on 2022-09-27 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_stock_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="StockDailyData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                ("date", models.DateField()),
                ("open", models.DecimalField(decimal_places=5, max_digits=10)),
                ("close", models.DecimalField(decimal_places=5, max_digits=10)),
                ("high", models.DecimalField(decimal_places=5, max_digits=10)),
                ("low", models.DecimalField(decimal_places=5, max_digits=10)),
                ("volume", models.DecimalField(decimal_places=5, max_digits=10)),
                (
                    "stock",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="daily_data",
                        to="core.stock",
                    ),
                ),
            ],
            options={
                "unique_together": {("stock", "date")},
            },
        ),
    ]
