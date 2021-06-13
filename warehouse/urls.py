from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'list/', views.WhListViewSet.as_view({"get": "list"}), name="WhList"),
    re_path(r'^list/(?P<pk>\d+)/$', views.WhListViewSet.as_view({
        'get': 'retrieve',
    }), name="WhList_1"),

    path(r'detail/', views.WhDetailViewSet.as_view({"get": "list"}), name="WhDetail"),
    re_path(r'^detail/(?P<pk>\d+)/$', views.WhDetailViewSet.as_view({
        'get': 'retrieve',
    }), name="WhDetail_1"),


]