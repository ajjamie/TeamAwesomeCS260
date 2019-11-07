from django import forms
from datetime import date

class MailingForm(forms.Form):
    id = forms.ImageField(widget = forms.HiddenInput(), required = False)
    dog = forms.CharField()
    first = forms.CharField()
    last = forms.CharField()
    email = forms.CharField()
    # Override the default field order, which is the declaration order
    field_order = ['dog', 'first', 'last','email']