from django import forms
from config.models import Kinesiologo, Deportista

class  KinesiologoForm(forms.ModelForm):
    class Meta:
        model = Kinesiologo
        exclude = []

class  DeportistaForm(forms.ModelForm):
    class Meta:
        model = Deportista
        exclude = []

        
        