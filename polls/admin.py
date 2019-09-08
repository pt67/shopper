from django.contrib import admin

from .models import Product
from .models import Food
from .models import Choice

admin.site.register(Product)
admin.site.register(Food)
admin.site.register(Choice)
