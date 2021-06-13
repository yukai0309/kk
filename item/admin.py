from django.contrib import admin
from .models import *


class ItListModelAd(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'quantity', 'sales_price', 'cost', 'weight',
                    'creater', 'create_time', 'update_time', 'description')
    search_fields = ('item_code', 'item_name')


admin.site.register(ItListModel, ItListModelAd)


class ItDetailModelAd(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'quantity', 'sales_price', 'cost', 'weight',
                    'creater', 'create_time', 'update_time', 'description')
    search_fields = ('item_code', 'item_name')


admin.site.register(ItDetailModel, ItDetailModelAd)
