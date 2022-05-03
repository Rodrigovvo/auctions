from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.v1.views import users, auctions


client = Client()
factory = APIRequestFactory()


class OfferTest(APITestCase):

    def setUp(self):
        self.data = {
            'id_customer': users.Person.objects.create(active=True).pk,
            'from': 'São Paulo - SP',
            'to': 'Belo Horizonte - MG',
            'initial_value': '120.00',
            'amount_type': 'TON',
            'amount': '50.00',
        }

    def test_create_offer(self):
        response = self.client.post('/api/v1/offers/', self.data, format='json')
        self.assertEqual(auctions.Offer.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['from'], self.data['from'])

    def test_update_offer_with_patch(self):
        self.client.post('/api/v1/offers/', self.data, format='json')
        self.assertEqual(auctions.Offer.objects.count(), 1)
        offer = auctions.Offer.objects.get(initial_value=self.data['initial_value'])
        response = self.client.patch(f'/api/v1/offers/{offer.pk}/', {'initial_value' : '150.00'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(offer.initial_value, '150.00')        

    def test_update_offer_with_put(self):
        self.client.post('/api/v1/offers/', self.data, format='json')
        self.assertEqual(auctions.Offer.objects.count(), 1)
        offer = auctions.Offer.objects.get(initial_value=self.data['initial_value'])
        self.data['initial_value'] = '150.00'
        response = self.client.put(f'/api/v1/offers/{offer.pk}/', self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertNotEqual(offer.initial_value, '150.00')

    def test_delete_offer(self):
        self.client.post('/api/v1/offers/', self.data, format='json')
        self.assertEqual(auctions.Offer.objects.count(), 1)
        offer = auctions.Offer.objects.get(amount=self.data['amount'])
        response = self.client.delete(f'/api/v1/offers/{offer.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(auctions.Bid.objects.count(), 0)
