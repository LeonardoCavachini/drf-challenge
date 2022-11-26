from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

from imoveis.models import Propertie


class AnunciosTests(APITestCase):
    anuncios_urls = reverse('anuncios')
    anuncio_url = reverse('anuncios-detail', args=[1])

    def setUp(self):
        self.user = User.objects.create(
            username='admin',
            password='123456hjyg'
        )
        self.property = Propertie.objects.create(
            limit_guests=8,
            bathroom_quantity=2,
            accept_animal=True,
            housekeeping_price=19.99,
            activate_date='2022-11-05'
        )
        self.data = {
            "platform_name": "plataform test",
            "platform_tax": 25.85,
            "property_code": self.property.property_code,
        }

    def get_authorization_headers(self):
        credentials = Token.objects.create(user=self.user)
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Token {credentials}'

    def tearDown(self):
        pass

    def test_get_anuncios(self):
        response = self.client.get(self.anuncios_urls)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_anuncios_authenticated(self):
        self.get_authorization_headers()

        response = self.client.post(
            self.anuncios_urls,
            self.data,
            format='json'
        )
        print(response.data['id'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['platform_name'], "plataform test")

    def test_post_anuncios_un_authenticated(self):
        response = self.client.post(
            self.anuncios_urls,
            self.data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_anuncio(self):
        self.get_authorization_headers()
        self.client.post(
            self.anuncios_urls,
            self.data,
            format='json'
        )
        response = self.client.get(self.anuncio_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['platform_name'], "plataform test")

    def test_delete_anuncio(self):
        self.get_authorization_headers()
        response = self.client.delete(self.anuncio_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
