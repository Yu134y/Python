from django import forms


class SampleForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=15, error_messages={'min_length': '名前は3文字以上で入力してください'})
    password = forms.CharField(required=False, max_length=20, widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=18, max_value=80)
    birthday = forms.DateField(required=False, input_formats=['%Y/%m/%d'])
