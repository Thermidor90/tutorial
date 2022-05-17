from django.urls import path
from . import views

app_name = 'thirdapp'

urlpatterns = [
    path('shop/', views.shop),
    path('jeju_olle/', views.jeju_olle, name='jejuolle'),
    path('jeju_olle/ajax/', views.jeju_olle_ajax),
    path('owner/', views.owner),
    path('hospital/', views.hospital),
]