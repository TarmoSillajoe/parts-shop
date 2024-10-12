from django.urls import path
from . import views

urlpatterns = [
    path("", views.applesauce, name="applesauce"),
    path("code-search-results", views.code_search_results, name="code-search-results"),
    path("merchants/", views.merchants, name="merchants"),
]
