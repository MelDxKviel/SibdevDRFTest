from rest_framework import serializers
from .models import Customer


class CustomerDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'spent_money')


class DealsFileSerializer(serializers.Serializer):
    file = serializers.FileField(allow_empty_file=False)
