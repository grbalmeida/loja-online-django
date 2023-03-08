from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True, unique=True)
    )

    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.CharField(max_length=200, db_index=True),
        description = models.TextField(blank=True)
    )
    
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    

    # No campo price, usamos DecimalField em vez de FloatField para evitar problemas de arredondamento

    # Sempre utilize DecimalField para armazenar valores monetários. FloatField usa o tipo float
    # de Python internamente, enquanto DecimalField utiliza o tipo Decimal. Ao usar o tipo
    # Decimal, evitamos problemas de arredondamento de float.
    price = models.DecimalField(max_digits=10, decimal_places=2)

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
        # ordering = ('name',)
        # index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])