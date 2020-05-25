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

        widgets = {
            'Nama' : forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Nama Lengkap'
                }
            ),

            'Brand' : forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),

            'TahunRilis' : forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Tahun rilis'
                }
            )
        }