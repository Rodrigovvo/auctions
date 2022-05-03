from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.serializers.auctions import BidSerializer, OfferSerializer
from apps.auctions.models import Bid, Offer


class OfferViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = Offer.objects.filter(customer__active=True).order_by('-modified_at')
    serializer_class = OfferSerializer
    permission_classes = []

    @action(detail=True, methods=['get'], name='get-bids',
    url_path='bids', url_name='get-bids')
    def get_bids(self, request, pk=None):
        """ 
        Action to returns serializer for active People
        
        :returns: (Response)
        """
        offer = self.get_object()
        bids = offer.bids.all().order_by('value')
        serializer_context = {
            'request': request,
        }

        page = self.paginate_queryset(bids)
        if page is not None:
            serializer = BidSerializer(
                page, many=True, context=serializer_context)
            return self.get_paginated_response(serializer.data)

        serializer = BidSerializer(
            bids, many=True, context=serializer_context)
        return Response(serializer.data)


class BidViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = []
