from django.urls import path
from . import views
urlpatterns = [
    path('',views.mainy,name='mainpage'),
    path('about/',views.abouty,name='aboutpage'),
    path('form/',views.formy,name='formpage'),
    path('WhoSigned?/',views.signy,name='signypage'),
]