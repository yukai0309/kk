from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'list/', views.InbListViewSet.as_view({"get": "list"}), name="InbList"),
    re_path(r'^list/(?P<pk>\d+)/$', views.InbListViewSet.as_view({
        'get': 'retrieve',
    }), name="InbList_1"),

    path(r'detail/', views.InbDetailViewSet.as_view({"get": "list"}), name="InbDetail"),
    re_path(r'^detail/(?P<pk>\d+)/$', views.InbDetailViewSet.as_view({
        'get': 'retrieve',
    }), name="InbDetail_1"),


]