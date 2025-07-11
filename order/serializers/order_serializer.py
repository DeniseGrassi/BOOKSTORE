from rest_framework import serializers
from order.models import Order
from product.models import Product
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        many=True
    )
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        return sum([product.price for product in instance.product.all()])

    def create(self, validated_data):
        product_data = validated_data.pop('products_id')
        # Captura o usuário autenticado do request
        user = self.context['request'].user

        order = Order.objects.create(user=user)
        order.product.set(product_data)

        return order

    class Meta:
        model = Order
        fields = ['product', 'total', 'products_id']
        extra_kwargs = {
            'product': {'required': False}
        }
