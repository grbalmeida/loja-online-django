from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

                # limpa o carrinho
                cart.clear()
                
                # dispara uma tarefa assíncrona
                order_created.delay(order.id)

                # define o pedido na sessão
                request.session['order_id'] = order.id

                # redireciona para o pagamento
                return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})