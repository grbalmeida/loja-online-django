import redis
from django.conf import settings
from .models import Product

# conecta com o redis

r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)

class Recommender(object):
    
    def get_product_key(self, id):
        return f'product:{id}:purchased_with'
    
    def products_bought(self, products):
        product_ids = [p.id for p in products]
        
        for product_id in product_ids:
            for with_id in product_ids:
                # obtém os outros produtos comprados com cada produto
                if product_id != with_id:
                    # incrementa a pontuação dos produtos comprados juntos
                    r.zincrby(self.get_product_key(product_id), 1, with_id)