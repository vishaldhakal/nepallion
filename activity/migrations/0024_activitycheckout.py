# Generated by Django 5.1 on 2025-01-15 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activity", "0023_alter_activity_accommodation_alter_activity_meals"),
    ]

    operations = [
        migrations.CreateModel(
            name="ActivityCheckout",
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
                ("full_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("country", models.CharField(max_length=100)),
                ("total_travelers", models.PositiveIntegerField()),
                ("departure_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("confirmed", "Confirmed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="checkouts",
                        to="activity.activity",
                    ),
                ),
            ],
            options={
                "verbose_name": "Activity Checkout",
                "verbose_name_plural": "Activity Checkouts",
                "ordering": ["-created_at"],
            },
        ),
    ]
