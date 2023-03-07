
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from product.models import product 
from product.serializers.product_serializers import productserializer

class Productviewset(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = productserializer
 
def get_queryset(self):
        
       return product.objects.all()
  
   