from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404 
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# class UserDetailView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True, context={'request': request})  # Include the 'context' parameter
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user, context={'request': request})  # Include the 'context' parameter
#         return Response(serializer.data)
