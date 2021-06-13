from rest_framework import viewsets
from .serializer import *


class WhListViewSet(viewsets.ModelViewSet):
    queryset = WhListModel.objects.all()
    serializer_class = WhListGetSerializer


class WhDetailViewSet(viewsets.ModelViewSet):
    queryset = WhDetailModel.objects.all()
    serializer_class = WhDetailGetSerializer
