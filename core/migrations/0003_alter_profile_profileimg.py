# Generated by Django 4.0.5 on 2023-04-06 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_pofileimg_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='user.png', upload_to='media'),
        ),
    ]
