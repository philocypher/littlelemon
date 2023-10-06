from django.urls import path,include
from . import views
from rest_framework import routers
app_name = 'api'

urlpatterns = [
    path('',views.index,name='index'),
    path('menu/', views.MenuItemsView.as_view(),name='menu-list'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
