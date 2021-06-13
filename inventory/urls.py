from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'list/', views.InvListViewSet.as_view({"get": "list"}), name="InvList"),
    re_path(r'^list/(?P<pk>\d+)/$', views.InvListViewSet.as_view({
        'get': 'retrieve',
    }), name="InvList_1"),

    path(r'detail/', views.InvDetailViewSet.as_view({"get": "list"}), name="InvDetail"),
    re_path(r'^detail/(?P<pk>\d+)/$', views.InvDetailViewSet.as_view({
        'get': 'retrieve',
    }), name="InvDetail_1"),


]