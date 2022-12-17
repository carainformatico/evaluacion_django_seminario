from django import forms
from seminarioAPP.models import seminario
from django.core import validators

class FormProyecto(forms.ModelForm):
    class Meta:
        model = seminario
        fields = '__all__'

