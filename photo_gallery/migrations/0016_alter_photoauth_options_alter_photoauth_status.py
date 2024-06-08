# Generated by Django 5.0.4 on 2024-06-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_gallery', '0015_alter_photoauth_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoauth',
            options={'ordering': ['-status', '-upload_date']},
        ),
        migrations.AlterField(
            model_name='photoauth',
            name='status',
            field=models.CharField(choices=[('1', 'Підтверджено'), ('3', 'Йде перевірка'), ('2', 'Відхилено')], default='3', max_length=31),
        ),
    ]
