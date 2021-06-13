from rest_framework import serializers
from .models import *


class ItListGetSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ItListModel


class ItListPostSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = ItListModel


class ItDetailGetSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    item_name = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = ItDetailModel


class ItDetailPostSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = ItDetailModel
