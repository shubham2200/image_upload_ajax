# Generated by Django 4.0.1 on 2022-01-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_user_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_image',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
