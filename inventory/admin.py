from django.contrib import admin
from .models import *


class InvListModelAd(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'quantity', 'sales_price', 'description',
                    'minimum_alert', 'maximum_alert', 'warehouse_code', 'warehouse_name')
    search_fields = ('item_code', 'item_name')


admin.site.register(InvListModel, InvListModelAd)


class InvDetailModelAd(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'quantity', 'sales_price', 'description',
                    'minimum_alert', 'maximum_alert', 'warehouse_code', 'warehouse_name')
    search_fields = ('item_code', 'item_name')


admin.site.register(InvDetailModel, InvDetailModelAd)
