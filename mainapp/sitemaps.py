from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from mainapp.models import Group, Product, Modification

class StaticViewSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return ['main_def','about', 'docs', 'contacts']

    def location(self, item):
        return reverse(item)


class GroupsSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return Group.objects.all()


class ProductsSitemap(Sitemap):
    protocol = 'https'

    def items(self):
        return Product.objects.all()

class ModificationsSitemap(Sitemap):
    protocol = 'https'
    
    def items(self):
        return Modification.objects.all()
