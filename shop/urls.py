from django.urls import path, re_path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail),
    # re_path(r'^(?P<pk>\d+)/$', views.item_detail),
    path('item/new/', views.item_new),
    path('item/<int:pk>/edit/', views.item_edit),
]