from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'list/', views.OtbListViewSet.as_view({"get": "list"}), name="OtbList"),
    re_path(r'^list/(?P<pk>\d+)/$', views.OtbListViewSet.as_view({
        'get': 'retrieve',
    }), name="OtbList_1"),

    path(r'detail/', views.OtbDetailViewSet.as_view({"get": "list"}), name="OtbDetail"),
    re_path(r'^detail/(?P<pk>\d+)/$', views.OtbDetailViewSet.as_view({
        'get': 'retrieve',
    }), name="OtbDetail_1"),


]