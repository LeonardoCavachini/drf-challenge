from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status

from imoveis.models import Propertie
from anuncios.models import Ad


class ReservasTests(APITestCase):
    reservas_urls = reverse('reservas-list')

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
        self.ad = Ad.objects.create(
            platform_name="nova platform",
            platform_tax=19.85,
            property_code=self.property
        )
        self.data = {
            "guests": 5,
            "ads_code": self.ad.id,
            "comments": "doing a simple test",
            "total_price": 25.85,
            "check_in": "2022-11-10",
            "check_out": "2022-12-26",
        }
        self.check_in_out = {
            "guests": 5,
            "ads_code": self.ad.id,
            "comments": "doing a simple test",
            "total_price": 25.85,
            "check_in": "2022-11-26",
            "check_out": "2022-11-10",
        }

    def get_authorization_headers(self):
        credentials = Token.objects.create(user=self.user)
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Token {credentials}'

    def tearDown(self):
        pass

    def test_get_reservas(self):
        response = self.client.get(
            self.reservas_urls,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_reserva_authenticated(self):
        self.get_authorization_headers()

        response = self.client.post(
            self.reservas_urls,
            self.data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['comments'], "doing a simple test")

    def test_post_reserva_un_authenticated(self):

        response = self.client.post(
            self.reservas_urls,
            self.data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_reserva_check_in_after_cjeck_out(self):
        self.get_authorization_headers()
        response = self.client.post(
            self.reservas_urls,
            self.check_in_out,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_reserva(self):
        self.get_authorization_headers()
        reservas = self.client.post(
            self.reservas_urls,
            self.data,
            format='json'
        )
        reservation_code = reservas.json()['reservation_code']
        reserva_url = reverse('reservas-detail', args=[reservation_code])

        response = self.client.get(reserva_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_reserva(self):
        self.get_authorization_headers()
        reservas = self.client.post(
            self.reservas_urls,
            self.data,
            format='json'
        )
        reservation_code = reservas.json()['reservation_code']
        reserva_url = reverse('reservas-detail', args=[reservation_code])

        response = self.client.patch(reserva_url, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_delete_reserva(self):
        self.get_authorization_headers()
        reservas = self.client.post(
            self.reservas_urls,
            self.data,
            format='json'
        )
        reservation_code = reservas.json()['reservation_code']
        reserva_url = reverse('reservas-detail', args=[reservation_code])
        response = self.client.delete(reserva_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
