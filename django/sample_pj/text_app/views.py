from django.http import HttpResponse  # Httpレスポンスクラスのインポート
from django.shortcuts import render, redirect  # テンプレート呼び出し用ショートカット関数のインポート
from django.views import generic  # 汎用クラスモジュールのインポート
from text_app.forms import SampleForm
from django.urls import reverse_lazy  # URL逆引き関数のインポート


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


# View関数によるコンテキスト設定
def set_context_render(request):
    # コンテキストオブジェクトの作成
    context = {
        'sample': 'sample-data',
        'sampleList': ['sample1', 'sample2', 'sample3']
    }
    return render(request,  # HTTPリクエストオブジェクト
                  'sample_output.html',  # テンプレートファイル（HTMLファイル）のパス
                  context)  # コンテキストオブジェクト


# 汎用クラスによるコンテキスト設定
# generic.TemplateViewのサブクラスを作成する
class SampleContextTemplateView(generic.TemplateView):
    template_name = 'sample_output.html'  # テンプレートファイルのパス

    def get_context_data(self, **kwargs):
        # スーパークラスからコンテキストの取得
        ctx = super().get_context_data(**kwargs)

        # 取得したコンテキストにデータを追加
        ctx['sample'] = 'sample_data'
        ctx['sampleList'] = ['sample1', 'sample2', 'sample3']

        # データ追加後のコンテキストを返す
        return ctx


def get_form_p3(request):
    param1 = request.POST['param1']
    param2 = request.POST['param2']
    result = int(param1) + int(param2)
    context = {
        'param1': param1,
        'param2': param2,
        'result': result,
    }
    return render(request, 'in_out.html', context)


# View関数によるコンテキスト設定（Form）
def disp_form(request):
    f = SampleForm()  # SampleFormオブジェクトの生成
    ctx = {'form': f}  # コンテキストへFormオブジェクトの登録
    return render(request, 'sample_form.html', ctx)


# 汎用クラスによるFormの表示
# generic.FormViewのサブクラスを作成する
class SampleFormView(generic.FormView):
    template_name = 'sample_form.html'  # テンプレートファイル（HTMLファイル）のパス
    form_class = SampleForm  # テンプレートで表示するフォームクラス名
    success_url = reverse_lazy('text_app:form_ok')  # アプリケーション名（app_name）：逆引き名（path関数のname引数で指定した名前）


# View関数によるFormデータの取得
def post_form(request):
    ctx = {}
    if request.method == 'post':  # 送信メソッドがPOSTだった場合
        f = SampleForm(request.POST)  # POSTデータからFormオブジェクトの生成
        # cleaned_dataオブジェクトからデータの取得
        if f.is_valid():  # 入力チェックOK時の処理
            name = f.cleaned_data['name']  # 文字列型で変換済み
            password = f.cleaned_data['password']  # 文字列型で変換済み
            age = f.cleaned_data['age']  # 整数型で変換済み
            birthday = f.cleaned_data['birthday']  # datetime型で変換済み
            # 取得した入力データを利用した処理
            ctx['msg'] = (name, password, age, birthday)
        else:  # 入力チェックNG時の処理
            ctx['msg'] = '入力エラーがあります'
    else:  # 送信メソッドがGETの場合（初回アクセス時）
        f = SampleForm()
    ctx['form'] = f
    return render(request, 'sample_form.html', ctx)


# 汎用クラスによるFormデータの取得
# generic.FormViewのサブクラスを作成する
class SampleFormView2(generic.FormView):
    template_name = 'sample_form.html'
    form_class = SampleForm

    # 入力チェックOK時の処理
    def form_valid(self, form):
        # cleaned_dataオブジェクトからデータの取得
        name = form.cleaned_data['name']
        password = form.cleaned_data['password']  # 文字列型で変換済み
        age = form.cleaned_data['age']  # 整数型で変換済み
        birthday = form.cleaned_data['birthday']  # datetime型で変換済み
        # 取得した入力データを利用した処理
        ctx = {'form': form, 'msg': (name, password, age, birthday)}
        # コンテキストを渡すためsuccess_urlを指定せず、render関数で画面遷移
        return render(self.request, self.template_name, ctx)

    # 入力チェックNG時の処理
    def form_invalid(self, form):
        ctx = {'form': form, 'msg': '入力エラーがあります'}
        return render(self.request, self.template_name, ctx)