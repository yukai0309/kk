from django.contrib import admin
from .models import *


class OtbListModelAd(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'quantity', 'sales_price', 'sender', 'receiver',
                    'creater', 'create_time', 'update_time', 'description')
    search_fields = ('item_code', 'item_name')


admin.site.register(OtbListModel, OtbListModelAd)


class OtbDetailModelAd(admin.ModelAdmin):
    list_display = ('item_code', 'item_name', 'quantity', 'sales_price', 'sender', 'receiver',
                    'creater', 'create_time', 'update_time', 'description')
    search_fields = ('item_code', 'item_name')


admin.site.register(OtbDetailModel, OtbDetailModelAd)
