from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# Create your views here.
from .models import *
from .permissions import IsAdminOrReadOnly
from .serializers import CustomUserSerializer
"""
class CustomUserViewSet(viewsets.ModelViewSet):

    serializer_class = CustomUserSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return CustomUser.objects.all()[:3]

        return CustomUser.objects.filter(pk = pk)

"""

class CustomUserAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CustomUserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)
class CustomUserAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminOrReadOnly,)


