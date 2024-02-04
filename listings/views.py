from django.shortcuts import render
from .serializers import ListingSerializer
from .models import Listing
from rest_framework import generics

# Create your views here.
class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

