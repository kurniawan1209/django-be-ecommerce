from django.contrib import admin
from .models import UserAdresses, UserBalances

admin.site.register([UserAdresses, UserBalances])