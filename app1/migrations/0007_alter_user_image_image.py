# Generated by Django 4.0.1 on 2022-01-13 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_user_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_image',
            name='image',
            field=models.FileField(upload_to='image/'),
        ),
    ]