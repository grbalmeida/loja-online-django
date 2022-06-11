from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Tarefa para enviar uma notificação por email quando
    quando um pedido for criado com sucesso.
    """

    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'

    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])

    return mail_sent