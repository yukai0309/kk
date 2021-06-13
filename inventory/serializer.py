from rest_framework import serializers
from .models import *


class InvListGetSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    warehouse_code = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = InvListModel


class InvListPostSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = InvListModel


class InvDetailGetSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    item_name = serializers.CharField(read_only=True, required=False)
    warehouse_code = serializers.CharField(read_only=True, required=False)
    warehouse_name = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = InvDetailModel


class InvDetailPostSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = InvDetailModel
