# Generated by Django 5.1.2 on 2024-12-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0012_remove_antisala_registro_geral_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registrogeral",
            name="data_criacao",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
