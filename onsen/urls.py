from django.urls import path,re_path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('result', views.result, name='result'),
    re_path("result/place=r''skin=r''efficacy=r''", views.result, name='result'),
    re_path("result/place=r''skin=r''efficacy=r''page=<int:num>", views.result, name='result'),   
]