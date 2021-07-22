# Generated by Django 3.1.1 on 2021-04-04 09:57

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0046_auto_20210331_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.TextField(blank=True, help_text='Описание для поисковой системы (160-200 знаков)', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='mod_table',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
