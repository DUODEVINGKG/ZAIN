# Generated by Django 5.1.5 on 2025-02-03 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_merge_0004_alter_base_whatsapp_0007_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='phone',
            field=models.CharField(max_length=155, verbose_name='Номер телеофона'),
        ),
    ]
