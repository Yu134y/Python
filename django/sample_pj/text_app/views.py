from django.http import HttpResponse  # Httpレスポンスクラスのインポート
from django.shortcuts import render, redirect  # テンプレート呼び出し用ショートカット関数のインポート
from django.views import generic  # 汎用クラスモジュールのインポート


# def welcome(request):
#     return HttpResponse('welcome')


def call_sample(request):
    return render(request,  # HTTPリクエストオブジェクト
                  'sample.html')  # テンプレートファイル（HTMLファイル）のパス


def call_redirect_sample(request):
    return redirect('https://github.com/Yu134y/')  # 移動先のURLパス


# generic.TemplateViewのサブクラスを作成する
class SampleTemplateView(generic.TemplateView):
    template_name = 'sample.html'  # テンプレートファイル（HTMLファイル）のパス


def get_param1(request, param1):
    return HttpResponse(param1)


def get_param2(request, param1=0, param2=0):
    return HttpResponse(param1 + param2)


def get_form_p1(request):
    param1 = request.GET['param1']
    param2 = request.GET['param2']
    return HttpResponse(f'param1: {param1} param2: {param2}')


def get_form_p2(request):
    param1 = request.POST['param1']
    param2 = request.POST['param2']
    return HttpResponse(f'param1: {param1} param2: {param2}')
