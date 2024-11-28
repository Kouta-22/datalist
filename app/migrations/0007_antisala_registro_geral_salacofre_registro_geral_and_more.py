# Generated by Django 5.1.2 on 2024-11-26 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_antisala_image_salacofre_image_salaenergia_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="antisala",
            name="registro_geral",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="antisala",
                to="app.registrogeral",
            ),
        ),
        migrations.AddField(
            model_name="salacofre",
            name="registro_geral",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sala_cofre",
                to="app.registrogeral",
            ),
        ),
        migrations.AddField(
            model_name="salaenergia",
            name="registro_geral",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sala_energia",
                to="app.registrogeral",
            ),
        ),
        migrations.AddField(
            model_name="salatelecom",
            name="registro_geral",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sala_telecom",
                to="app.registrogeral",
            ),
        ),
    ]
