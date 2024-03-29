"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from listings.views import ListingListView, ListingCreateView, ListingDetailView, ListingDeletelView, ListingUpdatelView
from users.api.views import ProfileDetailView, ProfileListView, ProfileUpdateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', ListingListView.as_view()),
    path('api/listings/create/', ListingCreateView.as_view()),
    path('api/listings/<int:pk>/', ListingDetailView.as_view()),
    path('api/listings/<int:pk>/delete/', ListingDeletelView.as_view()),
    path('api/listings/<int:pk>/update/', ListingUpdatelView.as_view()),
    
    path('api/profiles/', ProfileListView.as_view()),
    path('api/profiles/<int:seller>/', ProfileDetailView.as_view()),
    path('api/profiles/<int:seller>/update/', ProfileUpdateView.as_view()),
    
    # url for djoser
    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)