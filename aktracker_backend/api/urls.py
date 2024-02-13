from django.urls import path,include
from .views import ClientView, PartnerView
from rest_framework import routers

route = routers.DefaultRouter()
route1 = routers.DefaultRouter()
route.register('', ClientView, basename='clinetview')
route1.register('', PartnerView, basename='partnerview')

urlpatterns = [
    path('client/', include(route.urls)),
    path('partner/', include(route1.urls))
]