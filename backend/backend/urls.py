from django.urls import path, include
from rest_framework import routers

from api.v1.views import auctions, users


router = routers.DefaultRouter()
router.register(r'offers', auctions.OfferViewSet)
router.register(r'bids', auctions.BidViewSet)
router.register(r'persons', users.PersonViewSet)
router.register(r'enterprises', users.EnterpriseViewSet)
router.register(r'clients', users.ClientViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
