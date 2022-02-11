from rest_framework import views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerDealsSerializer, DealsFileSerializer
from .services import import_deals


class CustomerDealsAPIView(views.APIView):
    serializer_class = DealsFileSerializer

    def get(self, request, *args, **kwargs):
        queryset = Customer.objects.all()[:5]
        serializer_class = CustomerDealsSerializer
        response = {'response': serializer_class(queryset.all(), many=True).data}
        return Response(response, status=200)

    def post(self, request, *args, **kwargs):
        serializer = DealsFileSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            data = import_deals(file)
            return Response(data=data, status=200)
        else:
            data = {'Status': 'Error', 'Desc': serializer.errors['file']}
            return Response(data=data, status=400)
