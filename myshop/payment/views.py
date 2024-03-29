import braintree
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from orders.models import Order
from .tasks import payment_completed

# instancia o gateway de pagamentos Braintree
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        # obtém o nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # cria e submete a transação
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
                # Para que a transação seja automaticamente submetida para efetivação.
                'submit_for_settlement': True
            }
        })

        if result.is_success:
            # marca o pedido com pago
            order.paid = True
            # armazena o id de transação único
            order.braintree_id = result.transaction.id
            order.save()
            # dispara uma tarefa assíncrona
            # payment_completed.delay(order.id)
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # gera o token
        client_token = gateway.client_token.generate()

        return render(request, 'payment/process.html', {'order': order, 'client_token': client_token})

def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')