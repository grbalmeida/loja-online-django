from django import forms
from localflavor.us.forms import USZipCodeField
from localflavor.br.forms import BRZipCodeField
from .models import Order

class OrderCreateForm(forms.ModelForm):
    postal_code = BRZipCodeField()
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']