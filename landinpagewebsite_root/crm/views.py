from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceTable, PriceCard
from telebot.sendmessage import setTelegramm


# Create your views here.
def first_page(request):
    # object_list = Order.objects.all()
    # form = OrderForm()

    slider_list = CmsSlider.objects.all()

    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)

    price_table = PriceTable.objects.all()

    form = OrderForm()

    dict_objects = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form': form
    }
    return render(request, './index.html', dict_objects)


# обернем страницу на случай вдруг не было запроса, но к страанице обращаются
def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        setTelegramm(name, phone)
        return render(request, './thanks.html', {'name': name, })
    else:
        return render(request, './thanks.html')
