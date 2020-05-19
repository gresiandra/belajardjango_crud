from django import forms

from .models import smartphoneModel

class smartphoneForm(forms.ModelForm):
    class Meta:
        model = smartphoneModel
        fields = [
            'Nama',
            'Brand',
            'TahunRilis',
        ]