from django import forms
from .models import Habito

class HabitoForm(forms.ModelForm):
    data_inicial = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )
    data_final = forms.DateField(
        widget=forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY'}),
        input_formats=['%d/%m/%Y']
    )

    class Meta:
        model = Habito
        fields = ['nome', 'data_inicial', 'data_final']
