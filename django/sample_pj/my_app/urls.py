from django.urls import path
from my_app import views
from django.views import generic


app_name = 'my_app'

urlpatterns = [
    path('sample01/', views.call_sample, name='sample01'),
    path('sample01_redirect/', views.call_sample2, name='sample01_red'),
    # path('sample02/', views.CallSampleTemplateView.as_view(), name='sample02'),
    path('sample02/', generic.TemplateView.as_view(template_name='sample01.html'), name='sample02'),
    path('multi/', views.param_multiply, name='multi02'),
    path('multi/<int:param1>/<int:param2>/', views.param_multiply, name='multi01'),
    path('multi_i/', generic.TemplateView.as_view(template_name='multi_input.html'), name='multi_input'),
    path('multi_f/', views.param_multiply_form, name='multi_f'),
    path('multi_i2/', generic.TemplateView.as_view(template_name='multi_input2.html'), name='multi_input2'),
    path('multi_f2/', views.param_multiply_form2, name='multi_f2'),
    path('multi_i3/', generic.TemplateView.as_view(template_name='multi_input3.html'), name='multi_input3'),
    path('multi_f3/', views.param_multiply_form3, name='multi_f3'),
    path('form01/', views.MyAppFormView.as_view(template_name='form01.html'), name='form01')
]
