from django import forms
from config.models import Kinesiologo, Deportista, Tratamiento

class  KinesiologoForm(forms.ModelForm):
    class Meta:
        model = Kinesiologo
        exclude = []

class  DeportistaForm(forms.ModelForm):
    class Meta:
        model = Deportista
        exclude = []

class  TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        exclude = []


        
        