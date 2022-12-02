from io import BytesIO
from celery import task
# import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order

@task
def payment_completed(order_id):
    """
    Tarefa para enviar uma notificação por email
    quando um pedido é criado com sucesso.
    """
    
    order = Order.objects.get(id=order_id)
    
    # cria o email para a fatura
    subject = f'My Shop - EE Invoice no. {order.id}'
    message = f'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'admin@myshop.com', [order.email])
    
    # gera o pdf
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    # stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    # weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    # aneva o arquivo PDF
    email.attach(f'order_{order.id}.pdf', out.getvalue(), 'application/pdf')
    # envia o email
    email.send()