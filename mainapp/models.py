from django.db import models
from pytils.translit import slugify
from tinymce.models import HTMLField
from django.shortcuts import reverse
from multiselectfield import MultiSelectField

SENSOR_CHOICES = (('М', 'М'),
               ('У', 'У'),
               ('Р', 'Р'),
               ('И', 'И'),
               ('БЦА', 'БЦА'),
               ('БКП', 'БКП'),
               ('ЕД', 'ЕД'),

               ('БУМ', 'БУМ'),
               ('ЕДМ', 'ЕДМ'),)

DOCS_CATEGORIES_CHOICES = (
     ('Общепром', 'Общепром'),
     ('Взрыв', 'Взрыв'),
     ('Датчики и контроллеры', 'Датчики и контроллеры'),
     ('Пусковые и управляющие', 'Пусковые и управляющие'),
     ('Шлагбаумы', 'Шлагбаумы'),
)

class Group(models.Model):
    title       = models.CharField(max_length=250)
    position    = models.IntegerField('Позиция на странице каталога', unique=True)
    meta_description = models.TextField(null=True, blank=True)
    
    groups_content = HTMLField(null=True, blank=True, help_text='Блок информации показывается на каждой странице группы (для обобщенной информации)')
    name        = models.CharField('Название на странице группы', null=True, blank=True,max_length=250)
    img         = models.ImageField(upload_to='main_page', null=True, blank=True, help_text='размер 925x625, ppi 300 и вес не более 60кб')
    description = HTMLField(null=True, blank=True)
    slug        = models.CharField('url', unique=True, null=True, blank=True, max_length=200, help_text='например stance, "mechanisms/meo"' )
    pic_of_hat  = models.ImageField(upload_to='pic_of_hat', null=True, blank=True, help_text='size: 1920x500px')
    dark_banner = models.BooleanField(default=True)
    content     = HTMLField(null=True, blank=True)
    
    class Meta:
        ordering = ['position']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('SubgroupDetailView', args=[self.slug])

class Documentation(models.Model):
    name          = models.CharField(max_length=255)
    file          = models.FileField()
    document_category = models.CharField(choices=DOCS_CATEGORIES_CHOICES, max_length=255, null=True)
    key_filter    = models.CharField(max_length=20)
    key_sort      = models.IntegerField(null=True, blank=True, unique=True)

    class Meta:
        ordering = ['key_sort']

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    content      = HTMLField(help_text="синие подзаголовки - H4. Черные подзаговолки просто жирным")
    product_description = HTMLField(null=True, blank=True)
    mod_table    = HTMLField(null=True, blank=True)
    meta_description = models.TextField(help_text='Описание для поисковой системы (160-200 знаков)', null=True, blank=True)
    
    name         = models.CharField('Страница группы. Название', max_length=250)
    h1_mod       = models.CharField('Заголовок всех модификаций',max_length=250)

    href_title   = models.CharField("Превью. Название", max_length=250,)
    img          = models.ImageField('Превью. Картинка', upload_to='mechanisms_preview')
    description  = HTMLField('Превью. Описание', null=True, blank=True)

    sensors       = MultiSelectField(choices=SENSOR_CHOICES, max_choices=10, max_length=100, null=True, blank=True)
    parent       = models.ForeignKey(Group, on_delete=models.CASCADE)
    slug_product = models.SlugField('url', help_text='Например, "160" или "6_3"')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.href_title)

    def get_absolute_url(self):
        return reverse('ProductDetailView', kwargs={'slug':self.parent.slug,'slug_product':self.slug_product})

class ProductImage(models.Model):
    page = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mechanisms', null=True)
    first = models.BooleanField(default=False)

    class Meta:
        ordering = ('-first',)

    def __str__(self):
        return str(self.page.id)

class ProductDocs(models.Model):
    page = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item = models.ForeignKey(Documentation, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.page.name)



class Modification(models.Model):
    parent           = models.ForeignKey(Product, on_delete=models.CASCADE)
    title            = models.CharField(max_length=250, )
    slug_mod         = models.SlugField('url', null=True, blank=True, help_text='заполняется автоматически от title')
    content          = HTMLField(null=True, blank=True)

    class Meta:
        ordering = ['parent__id']

    def get_absolute_url(self):
        return reverse('ModificationDetailView', kwargs={'slug':self.parent.parent.slug,'slug_product':self.parent.slug_product,'slug_mod':self.slug_mod})

    def save(self, *args, **kwargs):
        self.slug_mod = slugify(self.title)
        super(Modification, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

class Certificate(models.Model):
    title   = models.CharField(max_length=200, null=True)
    picture = models.ImageField(upload_to='certificates/picture', null=True)
    file    = models.FileField(upload_to='certificates/file', null=True)

    def __str__(self):
        return str(self.title)

# этот класс содержит все варианты датчиков для исполнительных механизмов
# Данные из этого класс вытягиваются на страница продукта, модификации
class Sensor(models.Model):
    character   = models.CharField(choices=SENSOR_CHOICES, max_length=250)
    name        = models.CharField(max_length=50)
    description = models.TextField(max_length=700)
    icon_file        = models.FileField()


    def __str__(self):
        return str(self.name)
