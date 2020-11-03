from django import forms


class ShortenerForms(forms.Form):
    init_url = forms.CharField(widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "enter your URL"}),
                               label='Your URL')
    path = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your suggestion path'})
                           , required=False, label='your optional path')



