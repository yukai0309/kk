from rest_framework import viewsets
from .serializer import *


class InbListViewSet(viewsets.ModelViewSet):
    queryset = InbListModel.objects.all()
    serializer_class = InbListGetSerializer


class InbDetailViewSet(viewsets.ModelViewSet):
    queryset = InbDetailModel.objects.all()
    serializer_class = InbDetailGetSerializer
