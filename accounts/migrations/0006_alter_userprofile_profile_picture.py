# Generated by Django 3.2.7 on 2021-10-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='photos/thumbnail/empty.png', null=True, upload_to='user_profile/'),
        ),
    ]
