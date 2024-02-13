from django.shortcuts import render
from .models import Client, Partner
from .serializers import ClientSerializer, PartnerSerializer
from rest_framework import viewsets

# Create your views here.

class ClientView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class PartnerView(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
