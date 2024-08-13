from django.test import TestCase
from restaurant.views import *
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework import status

class MenuViewTest(TestCase):
    def setup(self):
        self.item1 = MenuItem.objects.create(title="Pizza Margherita", price=12.00, inventory=10)
        self.item2 = MenuItem.objects.create(title="Spaghetti Carbonara", price=15.00, inventory=20)
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        expected_data = serializer.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json; charset=utf-8')
        self.assertEqual(response.json(), expected_data)