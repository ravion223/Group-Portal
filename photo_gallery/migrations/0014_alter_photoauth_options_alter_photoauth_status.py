# Generated by Django 5.0.1 on 2024-06-06 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photo_gallery", "0013_alter_photoauth_options_alter_photoauth_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="photoauth",
            options={"ordering": ["status"]},
        ),
        migrations.AlterField(
            model_name="photoauth",
            name="status",
            field=models.CharField(
                choices=[
                    ("1", "Підтверджено"),
                    ("3", "Йде перевірка"),
                    ("2", "Відхилино"),
                ],
                default="0",
                max_length=31,
            ),
        ),
    ]
