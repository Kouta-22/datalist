# Generated by Django 5.1.2 on 2024-10-24 21:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AntiSala",
        ),
        migrations.DeleteModel(
            name="SalaCofre",
        ),
        migrations.DeleteModel(
            name="SalaEnergia",
        ),
        migrations.DeleteModel(
            name="SalaTelecom",
        ),
    ]
