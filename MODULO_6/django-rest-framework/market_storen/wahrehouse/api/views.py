from rest_framework import viewsets
from wahrehouse.models import Product
from wahrehouse.api.serializer import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticated]