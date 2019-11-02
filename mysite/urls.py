from django.urls import path

from .views import index, contact, portfolio

urlpatterns = [
    path('', index, name = 'home'),
    path('contact', contact, name = 'contact'),
    path('portfolio', portfolio, name = 'portfolio'),
]
