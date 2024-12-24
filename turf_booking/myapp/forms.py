from django import forms

from .models import EquipmentTable, turf

class equipmentform(forms.ModelForm):
    class Meta:
        model = EquipmentTable
        fields=['equipment','quantity','price','description']
    
# class turfregisterform(forms.ModelForm):
#     class Meta:
#         model = turf
#         fields=['name','phone','email','place']
class TurfForm(forms.ModelForm):
    slots = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter slots as comma-separated values (e.g., 9:00-10:00, 10:00-11:00)',
            'rows': 3
        }),
        label="Time Slots"
    )

    class Meta:
        model = turf
        fields = ['name', 'phone', 'image', 'email', 'address', 'location', 'rent', 'opentime', 'closingtime']

    def clean_slots(self):
        slots = self.cleaned_data.get('slots', '')
        if slots:
            # Validate slot format if necessary
            slot_list = [slot.strip() for slot in slots.split(',')]
            if not all(slot_list):
                raise forms.ValidationError("Please provide valid slots.")
        return slots
    