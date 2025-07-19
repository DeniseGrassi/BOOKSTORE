import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from order.factories import OrderFactory, UserFactory
from order.models import Order
from product.factories import CategoryFactory, ProductFactory


class TestOrderViewSet(APITestCase):
    def setUp(self):
        self.category = CategoryFactory(title="technology")
        self.product = ProductFactory(
            title="mouse", price=100, category=[self.category]
        )
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        response = self.client.get(reverse("order-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = response.json()  # mais limpo e seguro que json.loads
        order = order_data[0]  # assumindo que não há paginação

        self.assertEqual(order["product"][0]["title"], self.product.title)
        self.assertEqual(order["product"][0]["price"], self.product.price)
        self.assertEqual(order["product"][0]["active"], self.product.active)
        self.assertEqual(
            order["product"][0]["category"][0]["title"], self.category.title
        )

    def test_create_order(self):
        user = UserFactory()
        product = ProductFactory()

        data = {"products_id": [product.id], "user": user.id}

        response = self.client.post(
            reverse("order-list"), data=data, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)
        self.assertEqual(created_order.product.count(), 1)
        self.assertEqual(created_order.product.first().id, product.id)
