# Generated by Django 3.0.7 on 2020-09-07 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20200907_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='meta_keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modification',
            name='meta_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modification',
            name='meta_keywords',
            field=models.TextField(blank=True, null=True),
        ),
    ]
