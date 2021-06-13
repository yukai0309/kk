from rest_framework import viewsets
from .serializer import *


class ItListViewSet(viewsets.ModelViewSet):
    queryset = ItListModel.objects.all()
    serializer_class = ItListGetSerializer


class ItDetailViewSet(viewsets.ModelViewSet):
    queryset = ItDetailModel.objects.all()
    serializer_class = ItDetailGetSerializer
