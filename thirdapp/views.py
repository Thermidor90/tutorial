from django.shortcuts import render
from .models import Shop, JejuOlle

def jeju_olle(request):
    jeju_olle_list = JejuOlle.objects.all()
    print(jeju_olle_list)

    return render(
        request,
        'thirdapp/jeju_olle.html',
        {'jeju_olle_list': jeju_olle_list}
    )


def shop(request):
    shop_list = Shop.objects.all()
    
    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
    )
