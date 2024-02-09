from users.models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    # set up the id of profile to be if of seller
    lookup_field = 'seller'
    
class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    # set up the id of profile to be if of seller
    lookup_field = 'seller'
