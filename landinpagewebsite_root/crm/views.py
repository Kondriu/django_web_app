from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider


# Create your views here.
def first_page(request):
    # object_list = Order.objects.all()
    # form = OrderForm()

    slider_list = CmsSlider.objects.all()
    return render(request, './index.html', {
        'slider_list': slider_list,
        # 'object_list': object_list,
        # 'form': form
    })


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name = name, order_phone = phone)
    element.save()
    return render(request, './thank_page.html', {
        'name': name,
        'phone': phone
    })
