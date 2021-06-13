from django.db import models


class InvListModel(models.Model):
    item_code = models.CharField(max_length=200, verbose_name="貨物編號")
    item_name = models.CharField(max_length=200, verbose_name="貨物名稱")
    quantity = models.FloatField(default=0, verbose_name="數量")
    sales_price = models.FloatField(default=0, verbose_name="價格")
    description = models.CharField(max_length=255, verbose_name="說明")
    minimum_alert = models.FloatField(default=0, verbose_name="最低限額")
    maximum_alert = models.FloatField(default=0, verbose_name="最高限額")
    warehouse_code = models.CharField(max_length=200, verbose_name="倉庫編號")
    warehouse_name = models.CharField(max_length=200, verbose_name="倉庫名稱")

    class Mata:
        db_table = "InvList"

    def __str__(self):
        return self.item_code


class InvDetailModel(models.Model):
    item_code = models.CharField(max_length=200, verbose_name="貨物編號")
    item_name = models.CharField(max_length=200, verbose_name="貨物名稱")
    quantity = models.FloatField(default=0, verbose_name="數量")
    sales_price = models.FloatField(default=0, verbose_name="價格")
    description = models.CharField(max_length=255, verbose_name="說明")
    minimum_alert = models.FloatField(default=0, verbose_name="最低限額")
    maximum_alert = models.FloatField(default=0, verbose_name="最高限額")
    warehouse_code = models.CharField(max_length=200, verbose_name="倉庫編號")
    warehouse_name = models.CharField(max_length=200, verbose_name="倉庫名稱")

    class Mata:
        db_table = "InvDetail"

    def __str__(self):
        return self.item_code

