from django import forms


class VhostForm(forms.Form):
    ssenv = forms.CharField(max_length=60)
    path = forms.CharField(max_length=60)
    project = forms.CharField(max_length=60)
