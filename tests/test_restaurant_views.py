from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import RestaurantModel
from restaurant.serializer import RestaurantModelSerializer


class RestaurantModelTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.restaurant_data = {'name': 'Test Restaurant'}
        self.restaurant = RestaurantModel.objects.create(name='Test Restaurant')
        self.serializer = RestaurantModelSerializer(instance=self.restaurant)

    def test_get_all_restaurants(self):
        url = reverse('get-restaurants')
        response = self.client.get(url)
        restaurants = RestaurantModel.objects.all()
        serializer = RestaurantModelSerializer(restaurants, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_restaurant(self):
        url = reverse('rud-restaurant', kwargs={'pk': self.restaurant.id})
        response = self.client.get(url)
        serializer = RestaurantModelSerializer(self.restaurant)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_restaurant(self):
        url = reverse('create-restaurant')
        response = self.client.post(url, self.restaurant_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_restaurant(self):
        url = reverse('rud-restaurant', kwargs={'pk': self.restaurant.id})
        updated_data = {'name': 'Updated Restaurant Name'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_restaurant(self):
        url = reverse('rud-restaurant', kwargs={'pk': self.restaurant.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
