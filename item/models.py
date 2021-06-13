from django.db import models


class ItListModel(models.Model):
    item_code = models.CharField(max_length=200, verbose_name="貨物編號")
    item_name = models.CharField(max_length=200, verbose_name="貨物名稱")
    quantity = models.FloatField(default=0, verbose_name="數量")
    sales_price = models.FloatField(default=0, verbose_name="價格")
    cost = models.CharField(max_length=200, verbose_name="成本")
    weight = models.FloatField(default=0, verbose_name="重量")
    creater = models.CharField(max_length=255, verbose_name="建立者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="更新時間")
    description = models.CharField(max_length=255, verbose_name="說明")

    class Mata:
        db_table = "ItListModel"

    def __str__(self):
        return self.item_code


class ItDetailModel(models.Model):
    item_code = models.CharField(max_length=200, verbose_name="貨物編號")
    item_name = models.CharField(max_length=200, verbose_name="貨物名稱")
    quantity = models.FloatField(default=0, verbose_name="數量")
    sales_price = models.FloatField(default=0, verbose_name="價格")
    cost = models.CharField(max_length=200, verbose_name="成本")
    weight = models.FloatField(default=0, verbose_name="重量")
    creater = models.CharField(max_length=255, verbose_name="建立者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="更新時間")
    description = models.CharField(max_length=255, verbose_name="說明")

    class Mata:
        db_table = "ItDetailModel"

    def __str__(self):
        return self.item_code



