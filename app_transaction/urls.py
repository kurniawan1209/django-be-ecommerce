from rest_framework.routers import DefaultRouter
from .views import CartView, WishlistView, TransactionView

urlpatterns = []
router = DefaultRouter()

router.register("cart", CartView)
router.register("wishlist", WishlistView)
router.register("order", TransactionView)

urlpatterns += router.urls