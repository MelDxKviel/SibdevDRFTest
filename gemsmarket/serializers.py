from rest_framework import serializers
from .models import Customer


class CustomerDealsSerializer(serializers.ModelSerializer):
    gems = serializers.StringRelatedField(source='load_gems_list', many=True)

    class Meta:
        model = Customer
        fields = ('username', 'spent_money', 'gems')


class DealsFileSerializer(serializers.Serializer):
    file = serializers.FileField(allow_empty_file=False)
