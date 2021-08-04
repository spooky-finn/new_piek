# Generated by Django 3.1.7 on 2021-07-27 18:52

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('picture', models.ImageField(null=True, upload_to='certificates/picture')),
                ('file', models.FileField(null=True, upload_to='certificates/file')),
            ],
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
                ('document_category', models.CharField(choices=[('Общепром', 'Общепром'), ('Взрыв', 'Взрыв'), ('Датчики и контроллеры', 'Датчики и контроллеры'), ('Пусковые и управляющие', 'Пусковые и управляющие'), ('Шлагбаумы', 'Шлагбаумы')], max_length=255, null=True)),
                ('key_filter', models.CharField(max_length=20)),
                ('key_sort', models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                'ordering': ['key_sort'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('position', models.IntegerField(unique=True, verbose_name='Позиция на странице каталога')),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('groups_content', tinymce.models.HTMLField(blank=True, help_text='Блок информации показывается на каждой странице группы (для обобщенной информации)', null=True)),
                ('name', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название на странице группы')),
                ('img', models.ImageField(blank=True, help_text='размер 925x625, ppi 300 и вес не более 60кб', null=True, upload_to='main_page')),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('slug', models.CharField(blank=True, help_text='например stance, "mechanisms/meo"', max_length=200, null=True, unique=True, verbose_name='url')),
                ('pic_of_hat', models.ImageField(blank=True, help_text='size: 1920x500px', null=True, upload_to='pic_of_hat')),
                ('dark_banner', models.BooleanField(default=True)),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce.models.HTMLField(help_text='синие подзаголовки - H4. Черные подзаговолки просто жирным')),
                ('product_description', tinymce.models.HTMLField(blank=True, null=True)),
                ('mod_table', tinymce.models.HTMLField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, help_text='Описание для поисковой системы (160-200 знаков)', null=True)),
                ('name', models.CharField(max_length=250, verbose_name='Страница группы. Название')),
                ('h1_mod', models.CharField(max_length=250, verbose_name='Заголовок всех модификаций')),
                ('href_title', models.CharField(max_length=250, verbose_name='Превью. Название')),
                ('img', models.ImageField(upload_to='mechanisms_preview', verbose_name='Превью. Картинка')),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Превью. Описание')),
                ('sensors', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('М', 'М'), ('У', 'У'), ('Р', 'Р'), ('И', 'И'), ('БЦА', 'БЦА'), ('БКП', 'БКП'), ('ЕД', 'ЕД'), ('БУМ', 'БУМ'), ('ЕДМ', 'ЕДМ')], max_length=100, null=True)),
                ('slug_product', models.SlugField(help_text='Например, "160" или "6_3"', verbose_name='url')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.group')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(choices=[('М', 'М'), ('У', 'У'), ('Р', 'Р'), ('И', 'И'), ('БЦА', 'БЦА'), ('БКП', 'БКП'), ('ЕД', 'ЕД'), ('БУМ', 'БУМ'), ('ЕДМ', 'ЕДМ')], max_length=250)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=700)),
                ('icon_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='mechanisms')),
                ('first', models.BooleanField(default=False)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
            options={
                'ordering': ('-first',),
            },
        ),
        migrations.CreateModel(
            name='ProductDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.documentation')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Modification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug_mod', models.SlugField(blank=True, help_text='заполняется автоматически от title', null=True, verbose_name='url')),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
            options={
                'ordering': ['parent__id'],
            },
        ),
    ]