from django.db.models import OuterRef, Subquery, Sum, F
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Brands, Products, ProductCategories, ProductDetails, ProductInventories
from .serializers import BrandSerializer, ProductCategorySerializer, PrimaryProductSerializer, SecondayProductSerializer, ProductInventorySerializer


class ProductInventoryView(APIView):
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        key = request.query_params.get("key", None)
        if key in ["color", "size"]:
            datas = ProductInventories.objects.values("color", "size")
            result = []
            for data in datas:
                result.append(data[key])
            return Response(list(set(result)), status=200)
        return Response({"detail": "data not found"}, status=404)


class BrandView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = BrandSerializer
    queryset = Brands.objects.all()
    http_method_names = ["get"]

    def list(self, request):
        limit = int(request.query_params.get("limit", 0))
        page = int(request.query_params.get("page", 1))

        if limit and page:
            end = limit * page
            start = end - limit
            queryset = self.get_queryset()[start:end]
        else:
            queryset = self.get_queryset()
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductCategoryView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProductCategorySerializer
    queryset = ProductCategories.objects.all()

    def list(self, request):
        limit = int(request.query_params.get("limit", 0))
        page = int(request.query_params.get("page", 1))

        if limit and page:
            end = limit * page
            start = end - limit
            queryset = self.get_queryset()[start:end]
        else:
            queryset = self.get_queryset()
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class ProductView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = PrimaryProductSerializer
    queryset = Products.objects.all()
    http_method_names = ["get"]

    def list(self, request, pk=None):
        limit = int(request.query_params.get("limit", 0))
        page = int(request.query_params.get("page", 1))
        structure = request.query_params.get("structure", "detail")

        if limit and page:
            end = limit * page
            start = end - limit
            queryset = self.get_queryset()[start:end]
        else:
            queryset = self.get_queryset()
        
        if pk:
            queryset = queryset.filter(id=pk)

        image = ProductDetails.objects.filter(product=OuterRef("pk"))\
                .filter(key="images_0").values("value")
        price = ProductInventories.objects.filter(product=OuterRef("pk"))\
                [:1].values("price")
        
        queryset = queryset.annotate(image = Subquery(image))\
                    .annotate(price = Subquery(price))\
                    .annotate(total_stock = Sum("inv_product_keys__stock"))\
                    .annotate(brand_name = F("brand__name"))\
                    .annotate(category_name = F("category__name"))
                    
        serializer = self.get_serializer(queryset, many=True)
        if structure == "summary":
            serializer = SecondayProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        return self.list(request, pk=kwargs["pk"])