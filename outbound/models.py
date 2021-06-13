from django.db import models


class OtbListModel(models.Model):
    item_code = models.CharField(max_length=200, verbose_name="貨物編號")
    item_name = models.CharField(max_length=200, verbose_name="貨物名稱")
    quantity = models.FloatField(default=0, verbose_name="數量")
    sales_price = models.FloatField(default=0, verbose_name="價格")
    sender = models.CharField(max_length=200, verbose_name="發貨方")
    receiver = models.CharField(max_length=200, verbose_name="收貨方")
    creater = models.CharField(max_length=255, verbose_name="建立者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="更新時間")
    description = models.CharField(max_length=255, verbose_name="說明")

    class Meta:
        db_table = "OtbList"

    def __str__(self):
        return self.item_code


class OtbDetailModel(models.Model):
    item_code = models.CharField(max_length=200, verbose_name="貨物編號")
    item_name = models.CharField(max_length=200, verbose_name="貨物名稱")
    quantity = models.FloatField(default=0, verbose_name="數量")
    sales_price = models.FloatField(default=0, verbose_name="價格")
    sender = models.CharField(max_length=200, verbose_name="發貨方")
    receiver = models.CharField(max_length=200, verbose_name="收貨方")
    creater = models.CharField(max_length=255, verbose_name="建立者")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="更新時間")
    description = models.CharField(max_length=255, verbose_name="說明")

    class Meta:
        db_table = "OtbDetail"

    def __str__(self):
        return self.item_code


