from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)

    # No campo price, usamos DecimalField em vez de FloatField para evitar problemas de arredondamento

    # Sempre utilize DecimalField para armazenar valores monetários. FloatField usa o tipo float
    # de Python internamente, enquanto DecimalField utiliza o tipo Decimal. Ao usar o tipo
    # Decimal, evitamos problemas de arredondamento de float.
    price = models.DecimalField(max_digits=10, decimal_places=2)

    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name