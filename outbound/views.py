from rest_framework import viewsets
from .serializer import *


class OtbListViewSet(viewsets.ModelViewSet):
    queryset = OtbListModel.objects.all()
    serializer_class = OtbListGetSerializer


class OtbDetailViewSet(viewsets.ModelViewSet):
    queryset = OtbDetailModel.objects.all()
    serializer_class = OtbDetailGetSerializer
