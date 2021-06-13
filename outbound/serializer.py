from rest_framework import serializers
from .models import *


class OtbListGetSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    sender = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = OtbListModel


class OtbListPostSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    sender = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = OtbListModel


class OtbDetailGetSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    sender = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = OtbDetailModel


class OtbDetailPostSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    sender = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = OtbDetailModel
