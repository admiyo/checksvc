from django import forms

class ServiceForm(forms.Form):
    your_name = forms.CharField(label='service_url', max_length=100)
