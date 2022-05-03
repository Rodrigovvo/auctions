from decimal import Decimal
from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.v1.views import users, auctions


client = Client()
factory = APIRequestFactory()


class BidTest(APITestCase):

    def setUp(self):
        self.data = {
            'id_provider': users.Person.objects.create().pk,
            'id_offer': auctions.Offer.objects.create(initial_value=100, amount=100, customer_id=users.Person.objects.get(id=1).pk).pk,
            'value': '100.00',
            'amount': '50.00',
        }

    def test_create_bid(self):
        response = self.client.post('/api/v1/bids/', self.data, format='json')
        self.assertEqual(auctions.Bid.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['value'], self.data['value'])

    def test_update_bid_with_patch(self):
        self.client.post('/api/v1/bids/', self.data, format='json')
        self.assertEqual(auctions.Bid.objects.count(), 1)
        bid = auctions.Bid.objects.get(value=self.data['value'])
        response = self.client.patch(f'/api/v1/bids/{bid.pk}/', {'value' : Decimal('250')})
        bid = auctions.Bid.objects.get(amount=self.data['amount'])
        self.assertEqual(bid.value, Decimal('250.00'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_bid_with_put(self):
        self.client.post('/api/v1/bids/', self.data, format='json')
        self.assertEqual(auctions.Bid.objects.count(), 1)
        bid = auctions.Bid.objects.get(value=self.data['value'])
        self.data['value'] = Decimal('250.00')
        response = self.client.put(f'/api/v1/bids/{bid.pk}/', self.data)
        bid = auctions.Bid.objects.get(amount=self.data['amount'])
        self.assertEqual(bid.value, Decimal('250.00'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_bid(self):
        self.client.post('/api/v1/bids/', self.data, format='json')
        self.assertEqual(auctions.Bid.objects.count(), 1)
        bid_for_delete = auctions.Bid.objects.get(value=self.data['value'])

        response = self.client.delete(f'/api/v1/bids/{bid_for_delete.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(auctions.Bid.objects.count(), 0)
