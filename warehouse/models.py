from django.db import models


class WhListModel(models.Model):
    warehouse_code = models.CharField(max_length=200, verbose_name="倉庫編號")
    warehouse_name = models.CharField(max_length=200, verbose_name="倉庫名稱")
    address = models.CharField(max_length=200, verbose_name="地址")
    manager = models.CharField(max_length=255, verbose_name="管理者")
    contact_number = models.CharField(max_length=200, verbose_name="聯絡號碼")

    class Mata:
        db_table = "WhList"

    def __str__(self):
        return self.warehouse_code


class WhDetailModel(models.Model):
    warehouse_code = models.CharField(max_length=200, verbose_name="倉庫編號")
    warehouse_name = models.CharField(max_length=200, verbose_name="倉庫名稱")
    address = models.CharField(max_length=200, verbose_name="地址")
    manager = models.CharField(max_length=255, verbose_name="管理者")
    contact_number = models.CharField(max_length=200, verbose_name="聯絡號碼")

    class Mata:
        db_table = "WhDetail"

    def __str__(self):
        return self.warehouse_code
