from django.http import HttpResponse
from django.shortcuts import render
from .models import Hospital, Owner, Shop, JejuOlle


def owner(request):
    if request.method == 'POST':
        name = request.POST.get()

        owner = Owner(name=name)
        owner.save()

        return HttpResponse('주인 정보 등록 완료')
    return render(request, 'thirdapp/owner.html', {})

    

def jeju_olle(request):
    # jeju_olle_list = JejuOlle.objects.all()
    # print(jeju_olle_list)
    
    time = request.GET.get('time')
    if not time:
        time = ''
    
    jeju_olle_list = JejuOlle.objects.filter(
        time_info__contains = time
    )

    return render(
        request,
        'thirdapp/jeju_olle.html',
        {'jeju_olle_list': jeju_olle_list}
    )


def jeju_olle_ajax(request):
    return render(request, 'thirdapp/jeju_olle_ajax.html', {})


def shop(request):
    shop_list = Shop.objects.all()
    
    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
    )

def hospital(request):
    hospitals = Hospital.objects.all()
    return render(request, 'thirdapp/hospital.html', {'hospitals': hospitals})