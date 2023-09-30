from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserAddressSerializer, UserDetailSerializers
from .models import UserAdresses, UserDetails


class LogoutView(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT, data={"success"})
        except Exception as err:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"error"})
        

class UserAddressView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserAddressSerializer
    queryset = UserAdresses.objects.all()
    http_method_names = ["post", "get", "patch", "delete"]


class UserDetailsView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = UserDetailSerializers
    queryset = UserDetails.objects.all()
    http_method_names = ["post", "get", "patch", "delete"]

    def list(self, request):
        structure = request.query_params.get("structure", "detail")
        queryset = UserDetails.objects.get(user=request.user.id)
        address = UserAdresses.objects.filter(user=request.user.id)

        user = dict()
        if queryset:
            user = model_to_dict(queryset)
            
        user["id"] = user["user"]
        user["username"] = request.user.username
        user["first_name"] = request.user.first_name
        user["last_name"] = request.user.last_name

        del user["id"]
        user["address"] = []
        if structure == "detail":
            address_list = []
            for addr in address:
                address_list.append(model_to_dict(addr))
            user["address"] = address_list
        
        return Response(user, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        if int(kwargs["pk"]) != request.user.id:
            return Response({"detail": "Data not found"}, status=404)
        return self.list(request)
    
    def create(self, request):
        try:
            user = User.objects.create_user(username=request.data["username"], password=request.data["password"])
            user.first_name = request.data["first_name"]
            user.last_name = request.data["last_name"]
            user.email = request.data["email"]
            user.save()
            
            user_detail = {
                "user": user.id,
                "gender": request.data["gender"],
                "birth_date": request.data["birth_date"]
            }

            serializer = UserDetailSerializers(data=user_detail)
            if serializer.is_valid():
                serializer.save()

            result = {
                "id": user.id,
                "date_joined": user.date_joined,
                "username": user.username,
                "password": "********",
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            }
            return Response(result, status=201)
        except Exception as error:
            print("Error = ", error)
            return Response({"detail": "error"}, status=500)