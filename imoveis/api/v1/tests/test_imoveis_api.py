from django.urls import reverse
from django.contrib.auth.models import User


from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status


class ReservasTests(APITestCase):
    properties_urls = reverse('imoveis-list')

    def setUp(self):
        self.user = User.objects.create(
            username='admin',
            password='123456hjyg'
        )
        self.data = {
            "limit_guests": 5,
            "bathroom_quantity": 3,
            "accept_animal": False,
            "housekeeping_price": 25.85,
            "activate_date": "2022-11-10",
        }

    def get_authorization_headers(self):
        credentials = Token.objects.create(user=self.user)
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Token {credentials}'

    def tearDown(self):
        pass

    def test_get_properties(self):
        response = self.client.get(
            self.properties_urls,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_property_authenticated(self):
        self.get_authorization_headers()

        response = self.client.post(
            self.properties_urls,
            self.data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['housekeeping_price'], 25.85)

    def test_post_property_un_authenticated(self):

        response = self.client.post(
            self.properties_urls,
            self.data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_by_pk_property(self):
        self.get_authorization_headers()
        property = self.client.post(
            self.properties_urls,
            self.data,
            format='json'
        )
        property_code = property.json()['property_code']
        property_url = reverse('imoveis-detail', args=[property_code])

        response = self.client.get(property_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_property(self):
        self.get_authorization_headers()
        property = self.client.post(
            self.properties_urls,
            self.data,
            format='json'
        )
        data = {"accept_animal": True}
        property_code = property.json()['property_code']
        property_url = reverse('imoveis-detail', args=[property_code])

        response = self.client.patch(property_url, data=data, format='json')
        self.assertEqual(response.data['accept_animal'], True)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_property(self):
        self.get_authorization_headers()
        property = self.client.post(
            self.properties_urls,
            self.data,
            format='json'
        )
        property_code = property.json()['property_code']
        property_url = reverse('imoveis-detail', args=[property_code])
        response = self.client.delete(property_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
