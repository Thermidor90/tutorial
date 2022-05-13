from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show),
    path('army_shop/', views.army_shop),
    path('course/ajax/', views.course_ajax),
    path('army_shop/<int:year>/<int:month>/', views.army_shop2),
]
