from django.urls import path
from . import views

urlpatterns = [
    path("", views.applesauce, name="applesauce"),
    path("code-search-results", views.code_search, name="code-search-results"),
    path("merchants-found/", views.merchant_search, name="merchants-found"),
    path("invoice/", views.invoice, name="invoice"),
    path(
        "upload-invoice/<int:merchantid>/", views.upload_invoice, name="upload-invoice"
    ),
    path("processed-invoice/", views.processed_invoice, name="processed-invoice"),
]
