from django.urls import path
from . import views

urlpatterns = [
    path("", views.applesauce, name="applesauce"),
    path("cross/", views.cross_refs, name="cross_refs"),
    path("merchants/", views.merchants, name="merchants"),
    path("query/", views.code_query_form, name="code_query_form"),
]
