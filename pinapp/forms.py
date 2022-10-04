from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
    pincode = forms.IntegerField()
    class Meta:
        model = Address
        fields = ['name','pincode']