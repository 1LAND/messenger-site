# Generated by Django 4.1.5 on 2023-08-11 14:30

import Gallery.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.ImageField(blank=True, null=True, upload_to=Gallery.models.upload_to)),
            ],
        ),
    ]