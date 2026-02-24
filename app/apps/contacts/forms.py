from django import forms
from .models import BookingRequest

class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ["name", "phone", "service", "comment"]