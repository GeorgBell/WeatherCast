from django.urls import path
from weather_n_clothes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details_selection, name='details_form'),
    path('about/', views.about_view, name='about')
]
