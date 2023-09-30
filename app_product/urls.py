from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BrandView, ProductView, ProductCategoryView, ProductInventoryView

urlpatterns = [
    path("inventory", ProductInventoryView.as_view())
]
router = DefaultRouter()

router.register("item", ProductView)
router.register("brand", BrandView)
router.register("category", ProductCategoryView)

urlpatterns += router.urls