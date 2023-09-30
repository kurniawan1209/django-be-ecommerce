from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import LogoutView, UserAddressView, UserDetailsView

urlpatterns = [
    path("generate-token/", TokenObtainPairView.as_view()),
    path("refresh-token/", TokenRefreshView.as_view()),
    path("destroy-token/", LogoutView.as_view()),
]

router = DefaultRouter()

router.register("address", UserAddressView)
router.register("detail", UserDetailsView)

urlpatterns += router.urls