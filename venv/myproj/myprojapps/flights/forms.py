from django import forms
from .models import Flight
class HFlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = "__all__"
