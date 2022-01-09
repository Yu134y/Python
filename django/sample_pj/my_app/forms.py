from django import forms


class MyAppForm(forms.Form):
    p1 = forms.CharField()
    p2 = forms.IntegerField()
    p3 = forms.CharField(widget=forms.Textarea)
    p4 = forms.MultipleChoiceField(choices=(('1', '赤'), ('2', '黄'), ('3', '青')), widget=forms.CheckboxSelectMultiple)
    p5 = forms.ChoiceField(choices=(('1', '赤'), ('2', '黄'), ('3', '青')), widget=forms.RadioSelect)
    p6 = forms.ChoiceField(choices=(('1', '赤'), ('2', '黄'), ('3', '青')))
