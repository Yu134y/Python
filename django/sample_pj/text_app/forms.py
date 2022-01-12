import re

from django import forms
from text_app.models import Customer


class SampleForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=15, error_messages={'min_length': '名前は3文字以上で入力してください'})
    password = forms.CharField(required=False, max_length=20, widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=18, max_value=80)
    birthday = forms.DateField(required=False, input_formats=['%Y/%m/%d'])


class CustomerModelForm(forms.ModelForm):
    age = forms.IntegerField(min_value=10)  # モデルフィールドを上書きしたい場合

    class Meta:  # 詳細設定のためのMetaクラス
        model = Customer  # 更新対象のモデルクラス
        fields = ('name', 'age')  # fieldsまたはexcludes属性で表示カラムを指定


# ModelFormクラスを利用したカスタマイズ例
# class CustomerAccountModelForm(forms.ModelForm):
#     class Meta:  # 詳細設定のためのMetaクラス
#         model = CustomerAccount
#         fields = '__all__'  # モデル内のすべてのフィールドが利用できるように設定(id除く)
#         labels = {'email': 'メールアドレス', 'password': 'パスワード'}  # 表示名の変更
#         widgets = {'password': forms.PasswordInput(),}  # ウィジェットの変更
#
#         def clean_password(self):  # バリデーションのカスタマイズ
#             pwd = self.clean_password()['password']
#             # 入力チェック
#             if re.search(r'^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?¥d)[a-zA-Z¥d]{8,30}$', pwd) is None:
#                 self.add_error('password', 'パスワードは8文字以上で大文字・小文字・数字全てを使用しなければいけません')
#             return pwd
