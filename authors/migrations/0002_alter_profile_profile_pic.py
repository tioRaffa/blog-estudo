# Generated by Django 5.1.7 on 2025-04-02 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(
                default="profile_image/image/profile.png",
                upload_to="profile_image/image/%y/%m/%d",
                verbose_name="Foto de Perfil",
            ),
        ),
    ]
