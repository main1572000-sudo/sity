from django.urls import path
from . import views
urlpatterns = [
    path('',views.mainy,name='mainpage'),
    path('about/',views.shop,name='shoppage'),
    path('form/',views.formy,name='formpage'),
    path('WhoSigned?/',views.signy,name='signypage'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('info/<int:pk>/', views.info, name='info'),
]