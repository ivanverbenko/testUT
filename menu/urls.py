from django.urls import path

from menu.views import menu_view

urlpatterns = [
    path('<str:url>/', menu_view, name='menu_page'),
    path('', menu_view, name='menu_page'),
    ]