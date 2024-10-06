from django import forms


class CrossRefForm(forms.Form):
    code = forms.CharField(label="part code", max_length=50)
