from django.contrib import admin
from .models import *


class WhListModelAd(admin.ModelAdmin):
    list_display = ('warehouse_code', 'warehouse_name', 'address', 'manager', 'contact_number')
    search_fields = ('warehouse_code', 'warehouse_name')


admin.site.register(WhListModel, WhListModelAd)


class WhDetailModelAd(admin.ModelAdmin):
    list_display = ('warehouse_code', 'warehouse_name', 'address', 'manager', 'contact_number')
    search_fields = ('warehouse_code', 'warehouse_name')


admin.site.register(WhDetailModel, WhDetailModelAd)
