from django import forms


class SampleForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    age = forms.IntegerField()
    birthday = forms.DateField()