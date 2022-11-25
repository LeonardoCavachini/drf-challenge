from django.urls import path

from .views import AdsAPIView, AdAPIView

urlpatterns = [
    path('anuncios/', AdsAPIView.as_view(), name='anuncios'),
     path('anuncios/<int:pk>', AdAPIView.as_view(), name='anuncios') 
]