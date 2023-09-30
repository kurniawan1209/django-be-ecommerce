from django.db.models import F, Prefetch, Q
from django.forms.models import model_to_dict
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Carts, Wishlists, TrxHeaders, TrxLines
from app_product.models import ProductInventories
from .serializers import CartSerializer, WishlistSerializer, TrxHeaderSerializer, TrxLineSerializer, TransactionListSerializer

class CartView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = CartSerializer
    queryset = Carts.objects.all()
    http_method_names = ["post", "get"]

    def list(self, request):
        limit = int(request.query_params.get("limit", 0))
        page = int(request.query_params.get("page", 1))
        user = request.user.id
        queryset = Carts.objects.filter(user=user)

        if limit and page:
            end = limit * page
            start = end - limit
            queryset = queryset[start:end]
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        wishlist = ""
        product = ""

        if "wishlist" in request.data:
            param = request.data["wishlist"]
            wishlist = Wishlists.objects.filter(id__in=param)
            wishlists = list(wishlist.annotate(wishlist=F("id"))\
                            .values("product", "product_inv", "quantity", "user", "wishlist"))
            serializer = self.get_serializer(data=wishlists, many=True)

            if serializer.is_valid():
                serializer.save()
                wishlist.update(is_active=False)
                return Response(serializer.data, status=201)
            
        elif "product_inv" in request.data:
            param = request.data["product_inv"]
            products = ProductInventories.objects.filter(id__in=param)
            datas = []
            for product in products:
                
                data = {
                    "product": product.id,
                    "product_inv": product.id,
                    "user": request.user.id
                }
                datas.append(data)

            serializer = self.get_serializer(data=datas, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
        else:
            return Response({"status": "error"}, status=500)
        
        return Response(serializer.errors)
    
class WishlistView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = WishlistSerializer
    queryset = Wishlists.objects.all()
    http_method_names = ["post", "get"]

    def list(self, request):
        limit = int(request.query_params.get("limit", 0))
        page = int(request.query_params.get("page", 1))
        user = request.user.id
        queryset = Wishlists.objects.filter(user=user)

        if limit and page:
            end = limit * page
            start = end - limit
            queryset = queryset[start:end]
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class TransactionView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = TransactionListSerializer
    queryset = TrxHeaders.objects.all()
    http_method_names = ["post", "get", "patch"]

    def list(self, request):
        limit = int(request.query_params.get("limit", 0))
        page = int(request.query_params.get("page", 1))
        user = request.user.id
        queryset = TrxHeaders.objects.filter(user=user)

        if limit and page:
            end = limit * page
            start = end - limit
            queryset = queryset[start:end]
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        user = request.user.id
        try:
            cart_id = request.data["cart"]
        except:
            cart_id = 0
        header = request.data
        header["user"] = user

        # define line from cart_id or from posted data
        if cart_id:
            carts = Carts.objects.filter(pk__in=cart_id).values()
            lines = []
            for cart in carts:
                cart["product"] = cart["product_id"]
                cart["price"] = 0
                del cart["id"]; del cart["creation_date"]; del cart["user_id"]
                del cart["is_active"]; del cart["wishlist_id"]; del cart["product_id"]
                lines.append(cart)
        else:
            lines = request.data["lines"]

        # save header instance
        header_serializer = TrxHeaderSerializer(data=header)
        if header_serializer.is_valid():
            instance = header_serializer.save()
        else:
            return Response(header_serializer.errors, status=400)

        # save lines instance
        header_id = header_serializer.data["id"]
        for line in lines:
            line["header"] = header_id

            line_serializer = TrxLineSerializer(data=line)
            if line_serializer.is_valid():
                instance = line_serializer.save()
            else:
                return Response(line_serializer.errors, status=400)

        if cart_id:
            carts = Carts.objects.filter(pk__in=cart_id)
            for cart in carts:
                cart.is_active = False
                cart.save()

        # return new data
        queryset = TrxHeaders.objects.filter(id=header_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])