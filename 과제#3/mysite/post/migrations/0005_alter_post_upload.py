# Generated by Django 4.2.1 on 2023-05-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
