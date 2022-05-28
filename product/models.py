from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ColorModel(models.Model):
    code = models.CharField(max_length=7, verbose_name=_('code'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class SizeModel(models.Model):
    name = models.CharField(max_length=5, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('size')
        verbose_name_plural = _('sizes')


class TagModel(models.Model):
    name = models.CharField(max_length=54, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class ProductModel(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    image = models.ImageField(upload_to='products', verbose_name=_('img'))
    price = models.FloatField(verbose_name=_('price'))
    discount = models.PositiveIntegerField(verbose_name=_('discount'))
    description = models.TextField(verbose_name=_('description'))
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.RESTRICT, related_name='products', verbose_name=_('category'))
    color = models.ManyToManyField(
        ColorModel, related_name='products', verbose_name=_('color'), blank=True)
    size = models.ManyToManyField(
        SizeModel, related_name='products',  verbose_name=_('size'), blank=True)
    tag = models.ManyToManyField(TagModel, related_name='products', verbose_name=_('tag'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def get_price(self):
        if self.discount == 0:
            return self.price
        return (100 - self.discount) / 100 * self.price

    @property
    def is_discount(self):
        return self.discount

    def get_related(self):
        return ProductModel.objects.filter(category__name=self.category).exclude(pk=self.pk)[:4]

    @staticmethod
    def get_cart_info(cart):
        return ProductModel.objects.filter(id__in=cart)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
