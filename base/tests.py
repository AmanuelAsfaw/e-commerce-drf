from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .products import products
from .models import Product
class BaseTests(APITestCase):
    def setUp(self) -> None:
        for product in products:
            prdt = Product.objects.create(
                name= product['name'],
                image= product['image'],
                description= product['description'],
                brand= product['brand'],
                category= product['category'],
                price= product['price'],
                countInStock= product['countInStock'],
                rating= product['rating'],
                numReviews= product['numReviews']
            )
            prdt.save()
        
    def test_get_routes(self):
        """
        Ensure we can get list of 8 routes.
        """
        print('test_get_routes')
        url = reverse('routes')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 8)

    def test_get_products(self):
        """
        Ensure we can get list of 6 products.
        """
        print('test_get_products')
        url = reverse('products')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 6)

    def test_get_product(self):
        """
        Ensure we can get a single product detail.
        """
        print('test_get_product')
        url = reverse('products')
        
        response = self.client.get(url+'1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Airpods Wireless Bluetooth Headphones')