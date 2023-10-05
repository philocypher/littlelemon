from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'restaurant'

urlpatterns = [
    path('',views.index,name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
    # path('booking/',include(router.urls)),
]
