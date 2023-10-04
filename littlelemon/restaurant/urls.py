from django.urls import path,include
from . import views
from rest_framework import routers

app_name = 'restaurant'

urlpatterns = [
    path('',views.index,name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('booking/',include(router.urls)),
]
