from django import forms


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
                "hx-trigger": "input changed delay:500ms, search from:body",
            }
        ),
    )
