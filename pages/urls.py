from django.urls import path
from .views import HomePageView, AboutPageView, ExchangePageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('exchange', ExchangePageView.as_view(), name='exchange'),
    path('', HomePageView.as_view(), name='home'), 
    
]