from django import forms
from app1.models import customer
class inputform(forms.ModelForm):
    class Meta:
        model=customer
        fields=['first_name','last_name','adhar_no']