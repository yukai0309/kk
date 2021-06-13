from django.db import models


class InbListModel(models.Model):
    item_code = models.CharField(max_length=200, verbose_name="貨物編號")
    item_name = models.CharField(max_length=200, verbose_name="貨物名稱")
    quantity = models.FloatField(default=0, verbose_name="數量")
    sales_price = models.FloatField(default=0, verbose_name="價格")
    sender = models.CharField(max_length=200, verbose_name="發貨方")
    inbound_date = models.DateTimeField(auto_now_add=True, verbose_name="進貨日期")
    creater = models.CharField(max_length=255, verbose_name="建立者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="更新時間")
    description = models.CharField(max_length=255, verbose_name="說明")

    class Meta:
        db_table = "InbList"

    def __str__(self):
        return self.item_code


class InbDetailModel(models.Model):
    item_code = models.CharField(max_length=200, verbose_name="貨物編號")
    item_name = models.CharField(max_length=200, verbose_name="貨物名稱")
    quantity = models.FloatField(default=0, verbose_name="數量")
    sales_price = models.FloatField(default=0, verbose_name="價格")
    sender = models.CharField(max_length=200, verbose_name="發貨方")
    inbound_date = models.DateTimeField(auto_now_add=True, verbose_name="進貨日期")
    creater = models.CharField(max_length=255, verbose_name="建立者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="更新時間")
    description = models.CharField(max_length=255, verbose_name="說明")

    class Meta:
        db_table = "InbDetail"

    def __str__(self):
        return self.item_code
