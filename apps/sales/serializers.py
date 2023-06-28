from rest_framework import serializers
from apps.sales.models import OcOrder

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OcOrder
        fields = '__all__'
        depth = 2