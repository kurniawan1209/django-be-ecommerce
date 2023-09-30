from django.contrib import admin
from .models import Carts, TrxHeaders, TrxLines, TrxJourneys, TrxReviews, Wishlists

admin.site.register([
    Carts, TrxHeaders, TrxLines, TrxJourneys, TrxReviews, Wishlists
])