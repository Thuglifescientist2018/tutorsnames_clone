from django.urls import path
from .views import Pricing


urlpatterns = [
    path('', Pricing.as_view(), name='pricing')
]
