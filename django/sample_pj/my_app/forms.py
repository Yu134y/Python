from django import forms
from my_app.models import Product


class MyAppForm(forms.Form):
    p1 = forms.CharField()
    p2 = forms.IntegerField()
    p3 = forms.CharField(widget=forms.Textarea)
    p4 = forms.MultipleChoiceField(choices=(('1', '赤'), ('2', '黄'), ('3', '青')), widget=forms.CheckboxSelectMultiple)
    p5 = forms.ChoiceField(choices=(('1', '赤'), ('2', '黄'), ('3', '青')), widget=forms.RadioSelect)
    p6 = forms.ChoiceField(choices=(('1', '赤'), ('2', '黄'), ('3', '青')))


class MyAppForm2(forms.Form):
    param1 = forms.IntegerField(label='数値1', min_value=0, max_value=100,
                                error_messages={'min_value': '数値1には0以上100以下の整数を入力してください',
                                                'max_value': '数値1には0以上100以下の整数を入力してください'})
    operator = forms.ChoiceField(label='演算子', choices=((0, '+'), (1, '-'), (2, '×'), (3, '÷')))
    param2 = forms.IntegerField(label='数値2', min_value=0, max_value=100,
                                error_messages={'min_value': '数値2には0以上100以下の整数を入力してください',
                                                'max_value': '数値2には0以上100以下の整数を入力してください'})

    def clean(self):
        operator = self.cleaned_data['operator']
        param2 = self.cleaned_data['param2']
        if operator == '3' and param2 == 0:
            raise forms.ValidationError('割り算の場合は数値2に0を入力できません')


class ProductModelForm(forms.ModelForm):
    price = forms.IntegerField(min_value=0, label='単価')

    class Meta:
        model = Product
        fields = ('name', 'price', 'release_date')
        labels = {'name': '商品名', 'release_date': '発売日'}
