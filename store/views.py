from django.shortcuts import render
from rest_framework import viewsets

from .models import Store
from .serializers import StoreSerializer


# Create your views here.
class StoreVieSet(viewsets.ModelViewSet):
    queryset = Store.objects.all().order_by('created_at')
    serializer_class = StoreSerializer
