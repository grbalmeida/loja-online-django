import os
from celery import Celery

# define o módulo de configurações default de Django para o programa 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

# O atributo namespace especifica o prefixo que as configurações relacionadas ao Celery
# terão em nosso arquivo settings.py. Ao definir o namespace CELERY, todas as configurações
# do CELERY terão de incluir o prefixo CELERY_ em seus nomes (por exemplo, CELERY_BROKER_URL).
app.cofig_from_object('django.conf:settings', namespace='CELERY')

# O Celery procurará um arquivo tasks.py no diretório de cada aplicação adicionada em
# INSTALLED_APPS a fim de carregar as tarefas assíncronas aí definidas.
app.autodiscover_tasks()