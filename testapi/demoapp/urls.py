from rest_framework import routers
from django.urls import path,include
from .views import UserViewSet,UserDetailView
app_name = 'demoapp'


router = routers.SimpleRouter()
router.register(r'users', UserViewSet,basename='user-details')
# router.register(r'user', UserViewSet)


urlpatterns = [
    # path('users/<int:pk>', UserDetailView.as_view(),name='user-details'),
    path('',include(router.urls))
    # path('users/<int:pk>/', UserViewSet.as_view({'get':'retrieve'}), name='user-detail'),
]
# urlpatterns += router.urls
