from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('cats/<int:cat_id>/', views.categories, name='cats'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats_id'),
    path(r'archive/<year4:year>/', views.archive, name='archive'),
]

