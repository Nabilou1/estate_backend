from django.shortcuts import render
from .serializers import ListingSerializer
from .models import Listing
from rest_framework import generics

# Create your views here.
class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.all().order_by('-date_posted')
    serializer_class = ListingSerializer
    
class ListingCreateView(generics.CreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
class ListingDetailView(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
class ListingDeletelView(generics.DestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingUpdatelView(generics.UpdateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

