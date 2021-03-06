# Generated by Django 3.2.7 on 2021-10-02 22:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('cat_image', models.ImageField(blank=True, upload_to='photos/categories')),
                ('thumbnail', models.ImageField(blank=True, upload_to='photos/thumbnail')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
    ]
