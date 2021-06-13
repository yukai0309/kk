from rest_framework import serializers
from .models import *


class WhListGetSerializer(serializers.ModelSerializer):
    warehouse_code = serializers.CharField(read_only=True, required=False)
    manager = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = WhListModel


class WhListPostSerializer(serializers.ModelSerializer):
    warehouse_code = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = WhListModel


class WhDetailGetSerializer(serializers.ModelSerializer):
    warehouse_code = serializers.CharField(read_only=True, required=False)
    warehouse_name = serializers.CharField(read_only=True, required=False)
    manager = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = WhDetailModel


class WhDetailPostSerializer(serializers.ModelSerializer):
    warehouse_code = serializers.CharField(read_only=True, required=False)
    warehouse_name = serializers.CharField(read_only=True, required=False)
    manager = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = WhDetailModel
