from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone'}), required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message'}))