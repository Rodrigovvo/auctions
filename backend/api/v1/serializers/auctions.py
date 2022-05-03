from typing import OrderedDict
from rest_framework import serializers

from apps.auctions.models import Bid, Offer
from apps.users.models import Person
from api.v1.serializers.users import PersonSerializer


class OfferSerializer(serializers.ModelSerializer):
    """ Serializer for Offers """
    
    id_customer = serializers.PrimaryKeyRelatedField(queryset = Person.objects.all(), source='customer')
    _from = serializers.CharField(source='location_from', label='from')
    to = serializers.CharField(source='location_to')

    class Meta:
        model = Offer
        fields = [
            'id', 'id_customer', '_from', 'to', 
            'initial_value', 'amount', 'amount_type'
        ]

    def get_fields(self) -> OrderedDict:
        """ Get fields to Meta.fields. Change the namefield for needed fields. 

        :return: A dict with namefield and the serializer field
        :rtype: OrderedDict
        """

        fields = super().get_fields()
        _from = fields.pop('_from', None)
        fields['from'] = _from
        return fields

    def to_representation(self, instance):
        data = super(OfferSerializer, self).to_representation(instance)
        data['id_customer'] = PersonSerializer(instance.customer).data
        return data

class BidSerializer(serializers.ModelSerializer):
    """ Serializer for Bids """

    id_provider = serializers.PrimaryKeyRelatedField(queryset = Person.objects.all(), source='provider')
    id_offer = serializers.PrimaryKeyRelatedField(queryset = Offer.objects.all(), source='offer')
    
    class Meta:
        model = Bid
        fields = [
            'id', 'id_provider', 'id_offer', 'value', 'amount',
        ]

    def to_representation(self, instance):
        data = super(BidSerializer, self).to_representation(instance)
        data['id_provider'] = PersonSerializer(instance.provider).data
        return data