from django.urls import path, register_converter, re_path  # URL指定用関数のインポート
from text_app import views, converters  # アプリケーションパッケージのviews, convertersモジュール
from django.views import generic


app_name = 'text_app'  # アプリケーションの逆引き名（省略可）

register_converter(converters.FourDigityearConverter, 'yyyy')

urlpatterns = [
    # path('welcome/',  # URL設定
    #      views.welcome,  # View関数名
    #      name='wel'),  # 逆引き名
    path('sample/', views.call_sample, name='sample'),
    path('sample_redirect/', views.call_redirect_sample, name='sample_red'),
    path('sample_tmp/',
         views.SampleTemplateView.as_view(),  # as_view()メソッド
         # generic.TemplateView.as_view(template_name='sample.html')  直接URL定義へ汎用クラスの設定を書き込むことも可能
         name='sample_tmp'),
    path('get_p/<str:param1>/',  # URL設定（パラメータ設定含む <パスコンバータ:引数名>）
         views.get_param1,
         name='get_p1'),
    path('get_pc/<yyyy:param1>/', views.get_param1, name='get_pc'),
    # パスコンバータを自作するのではなく、正規表現を利用してパターンなどを指定することも可能
    re_path('get_p2/(?P<param1>[0-9]+)/(?P<param2>[0-9]+)', views.get_param2, name='get_p2'),  # パラメータを取得する場合のURL
    path('get_p2/', views.get_param2, name='get_p2_d'),  # デフォルト値を利用する場合のURL
    path('input/', generic.TemplateView.as_view(template_name='input.html'), name='input'),
    path('get_form1/', views.get_form_p1, name='form01'),
    path('input2/', generic.TemplateView.as_view(template_name='input2.html'), name='input2'),
    path('get_form2/', views.get_form_p2, name='form02'),
    path('output/', views.set_context_render, name='ctx_01'),
    path('output2/', views.SampleContextTemplateView.as_view(), name='ctx_02'),
    path('in_out01/', generic.TemplateView.as_view(template_name='in_out.html'), name='in_out01'),
    path('in_out02/', views.get_form_p3, name='in_out02'),
    path('parents/', generic.TemplateView.as_view(template_name='parents.html'), name='parents'),
    path('child/', generic.TemplateView.as_view(template_name='child.html'), name='child'),
    path('sample_form/', views.disp_form, name='disp_form'),
    path('sample_form_v/', views.SampleFormView.as_view(), name='disp_form2'),
    path('form_ok/', generic.TemplateView.as_view(template_name='form_ok.html'), name='form_ok'),
]
