from django.test import Client
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from api.v1.views import users


client = Client()
factory = APIRequestFactory()


class ClientTest(APITestCase):

    def test_create_client(self):
        data = {
                'name': 'Test Name',
                'about': 'Description about client',
                'doc': '800.186.880-04',
                'active': True,
                'site': "https://www.django-rest-framework.org/",
        }

        response = self.client.post('/api/v1/clients/', data, format='json')
        self.assertEqual(users.Client.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])

    def test_update_client_with_patch(self):
        data = {
                'name': 'Test Name',
                'about': 'Description about client',
                'doc': '800.186.880-04',
                'active': True,
                'site': "https://www.django-rest-framework.org/",
        }

        self.client.post('/api/v1/clients/', data, format='json')
        self.assertEqual(users.Client.objects.count(), 1)
        client = users.Client.objects.get(name=data['name'])
        response = self.client.patch(f'/api/v1/clients/{client.pk}/', {'name' : 'Other Name Patch'})
        client = users.Client.objects.get(about=data['about'])
        self.assertEqual(client.name, 'Other Name Patch')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_client_with_put(self):
        data = {
                'name': 'Test Name',
                'about': 'Description about client',
                'doc': '800.186.880-04',
                'active': True,
                'site': "https://www.django-rest-framework.org/",
        }

        self.client.post('/api/v1/clients/', data, format='json')
        self.assertEqual(users.Client.objects.count(), 1)
        client = users.Client.objects.get(name=data['name'])
        data['name'] = 'Other Name Put'
        response = self.client.put(f'/api/v1/clients/{client.pk}/', data=data)
        client = users.Client.objects.get(about=data['about'])
        self.assertEqual(client.name, 'Other Name Put')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_client(self):
        data = {
                'name': 'Test Name',
                'about': 'Description about client',
                'doc': '800.186.880-04',
                'active': True,
                'site': "https://www.django-rest-framework.org/",
        }

        self.client.post('/api/v1/clients/', data, format='json')
        self.assertEqual(users.Client.objects.count(), 1)
        client_for_delete = users.Client.objects.get(name=data['name'])

        response = self.client.delete(f'/api/v1/clients/{client_for_delete.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        client_deleted = users.Client.objects.get(name=data['name'])
        self.assertEqual(False, client_deleted.active)
