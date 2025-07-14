from django.test import TestCase
from product.models import Category, Product
from product.serializers import ProductSerializer


class ProductSerializerTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Livros", slug="livros")

        self.product = Product.objects.create(
            title="Livro Django", description="Um ótimo livro sobre Django", price=59.9
        )
        self.product.category.set([self.category])

    def test_product_serializer(self):
        serializer = ProductSerializer(instance=self.product)
        self.assertEqual(serializer.data["title"], "Livro Django")
