from django.contrib import admin
from .models import Listing, Poi
#from .forms import ListingsForm
from .forms import PoisForm

#class ListingAdmin(admin.ModelAdmin):
 #   form = ListingsForm

class PoiAdmin(admin.ModelAdmin):
    form = PoisForm
 
# Register your models here.
#admin.site.register(Listing, ListingAdmin)
admin.site.register(Listing)
admin.site.register(Poi, PoiAdmin)