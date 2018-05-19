from rest_framework import generics
from .models import Sale 
from .serializers import SaleSerializer

class SaleListApi(generics.ListAPIView):
    serializer_class = SaleSerializer

    def get_queryset(self):
        return Sale.objects.all()
