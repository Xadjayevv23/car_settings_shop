from modeltranslation.translator import register, TranslationOptions
from .models import ProductModel


@register(ProductModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')



