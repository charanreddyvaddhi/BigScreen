from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.page1, name='homepage'),
    path('world/',views.page2, name='worldpage'),
    path('india/',views.page3, name='indiapage'),
    path('media/',views.page4, name='mediapage'),
    path('worldnews/',views.page5, name='worldnews'),
    path('worldmovies/',views.page6, name='worldmovies'),
    path('worldbusiness/',views.page7,name='worldbusiness'),
    path('indianews/',views.page8, name='indianews'),
    path('indiamovies/',views.page9, name='indiamovies'),
    path('indiabusiness/',views.page10, name='indiabusiness'),

]
