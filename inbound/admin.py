from django.contrib import admin
from .models import *


class InbListModelAd(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'quantity', 'sales_price', 'sender',
                    'creater', 'create_time', 'inbound_date', 'update_time', 'description')
    search_fields = ('item_code', 'item_name')


admin.site.register(InbListModel, InbListModelAd)


class InbDetailModelAd(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'quantity', 'sales_price', 'sender',
                    'creater', 'create_time', 'inbound_date', 'update_time', 'description')
    search_fields = ('item_code', 'item_name')


admin.site.register(InbDetailModel, InbDetailModelAd)
