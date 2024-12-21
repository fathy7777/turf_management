from django import forms

from .models import EquipmentTable

class equipmentform(forms.ModelForm):
    class Meta:
        model = EquipmentTable
        fields=['equipment','quantity','price','description']
    