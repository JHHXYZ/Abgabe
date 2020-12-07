import json
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.db.models import Q
from .models import MenuItem, Category, OrderModel


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class Covid(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/covid.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        vorspeisen = MenuItem.objects.filter(
            category__name__contains='vorspeisen')
        hauptgerichte = MenuItem.objects.filter(category__name__contains='hauptgerichte')
        desserts = MenuItem.objects.filter(category__name__contains='desserts')
        getränke = MenuItem.objects.filter(category__name__contains='getränke')

        context = {
            'vorspeisen': vorspeisen,
            'hauptgerichte': hauptgerichte,
            'desserts': desserts,
            'getränke': getränke,
        }

        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')

        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            zip_code=zip_code,
            
        )
        order.items.add(*item_ids)

        body = ('Danke für Ihre Bestellung! Ihr Essen wird bald geliefert\n'
                f'Totale Kosten: {price}\n'
                'Guten Appetit!')

        send_mail(
            'Danke für Ihre Bestellung!',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )

        context = {
            'items': order_items['items'],
            'price': price
        }

        return redirect('order-confirmation', pk=order.pk)


class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment-confirmation')


class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_confirmation.html')


class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)


class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)

