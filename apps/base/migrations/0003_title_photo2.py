# Generated by Django 5.1.5 on 2025-01-24 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='photo2',
            field=models.ImageField(default=1, upload_to='photo', verbose_name='Вторая Фотография'),
            preserve_default=False,
        ),
    ]
