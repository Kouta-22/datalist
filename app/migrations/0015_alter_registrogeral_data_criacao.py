# Generated by Django 5.1.2 on 2024-12-18 21:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0014_alter_registrogeral_data_criacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registrogeral",
            name="data_criacao",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]