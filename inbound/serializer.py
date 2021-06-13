from rest_framework import serializers
from .models import *


class InbListGetSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    sender = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = InbListModel


class InbListPostSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    sender = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = InbListModel


class InbDetailGetSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    sender = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = InbDetailModel


class InbDetailPostSerializer(serializers.ModelSerializer):
    item_code = serializers.CharField(read_only=True, required=False)
    sender = serializers.CharField(read_only=True, required=False)
    creater = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = InbDetailModel
