from rest_framework import viewsets
from .serializer import *


class InvListViewSet(viewsets.ModelViewSet):
    queryset = InvListModel.objects.all()
    serializer_class = InvListGetSerializer


class InvDetailViewSet(viewsets.ModelViewSet):
    queryset = InvDetailModel.objects.all()
    serializer_class = InvDetailGetSerializer
