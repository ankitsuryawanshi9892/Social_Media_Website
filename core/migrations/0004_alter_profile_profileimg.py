# Generated by Django 4.0.5 on 2023-04-06 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='user.png', upload_to='profile_images'),
        ),
    ]
