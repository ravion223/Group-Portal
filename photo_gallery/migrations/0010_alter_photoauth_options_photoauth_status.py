# Generated by Django 5.0.1 on 2024-06-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photo_gallery", "0009_alter_photopost_options_photoauth_details_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="photoauth",
            options={"ordering": ["-upload_date", "authorized"]},
        ),
        migrations.AddField(
            model_name="photoauth",
            name="status",
            field=models.CharField(
                choices=[
                    ("1", "Підтверджено"),
                    ("0", "Потрібна перевірка"),
                    ("-1", "Відхилино"),
                ],
                default="0",
                max_length=31,
            ),
        ),
    ]
