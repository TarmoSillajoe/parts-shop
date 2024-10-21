from django import forms
from django.urls import reverse_lazy


class UploadInvoiceForm(forms.Form):
    file = forms.FileField(label="vali csv-fail")


class MerchantSearchForm(forms.Form):
    name = forms.CharField(
        label="firma nimi",
        max_length=100,
        widget=forms.TextInput(
            {
                "class": "form-input mt-1 block w-full rounded-md border border-gray-900",
                "placeholder": "firma",
                "hx-get": reverse_lazy("merchants-found"),
                "hx-target": "#merchants-found",
                "hx-trigger": "input changed delay:500ms, search from:body",
            }
        ),
    )


class CrossRefForm(forms.Form):
    code = forms.CharField(
        label="part code",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-input mt-1 block w-full rounded-md border border-gray-900",
                "placeholder": "kood",
                "hx-get": "code-search-results",
                "hx-target": "#codes-found",
                "hx-include": "#id_code",
                "hx-trigger": "input changed delay:700ms, search from:body",
            }
        ),
    )
