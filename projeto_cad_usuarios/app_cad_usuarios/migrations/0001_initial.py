# Generated by Django 4.2.2 on 2023-06-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuarios",
            fields=[
                ("id_usuario", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.TextField(max_length=255)),
                ("idade", models.IntegerField()),
            ],
        ),
    ]
