from django.urls import path
from . import views



app_name = 'firstapp'

urlpatterns = [
    # path('form/model/', views.form_model),

    path('main/', views.main),
    path('insert/', views.insert),
    path('show/', views.show, name='show'),
    path('req/get/', views.req_get),
    path('req/post/', views.req_post, name='post'),
    path('static/', views.static),
    
    # ajax를 동작시키기 위한 프런트 페이지 보여주기
    path('req/ajax4/', views.req_ajax4),

    path('var/', views.var),
    path('tag/', views.tag),
    path('filter/', views.filter),

    path('template/', views.template),
]
