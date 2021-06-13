from django.urls import path, re_path
from . import views

urlpatterns = [
    path(r'list/', views.ItListViewSet.as_view({"get": "list"}), name="ItList"),
    re_path(r'^list/(?P<pk>\d+)/$', views.ItListViewSet.as_view({
        'get': 'retrieve',
    }), name="ItList_1"),

    path(r'detail/', views.ItDetailViewSet.as_view({"get": "list"}), name="ItDetail"),
    re_path(r'^detail/(?P<pk>\d+)/$', views.ItDetailViewSet.as_view({
        'get': 'retrieve',
    }), name="ItDetail_1"),


]