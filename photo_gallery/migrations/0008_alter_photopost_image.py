# Generated by Django 5.0.1 on 2024-06-05 09:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "photo_gallery",
            "0007_alter_photoauth_photo_post_alter_photopost_image_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="photopost",
            name="image",
            field=models.ImageField(upload_to="photo-gallery/"),
        ),
    ]
