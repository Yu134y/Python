from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from my_app.forms import MyAppForm


def call_sample(request):
    return render(request, 'sample01.html')


def call_sample2(request):
    return redirect('http://127.0.0.1:8000/myapp/sample01')


class CallSampleTemplateView(generic.TemplateView):
    template_name = 'sample01.html'


def param_multiply(request, param1=0, param2=0):
    return HttpResponse(param1 * param2)


def param_multiply_form(request):
    param1 = request.GET['param1']
    param2 = request.GET['param2']
    return HttpResponse(int(param1) * int(param2))


def param_multiply_form2(request):
    param1 = request.POST['param1']
    param2 = request.POST['param2']
    return HttpResponse(int(param1) * int(param2))


def param_multiply_form3(request):
    param1 = request.POST['param1']
    param2 = request.POST['param2']
    operator = request.POST['operator']
    if operator == '0':
        symbol = '+'
        result = int(param1) + int(param2)
    elif operator == '1':
        symbol = '-'
        result = int(param1) - int(param2)
    elif operator == '2':
        symbol = '×'
        result = int(param1) * int(param2)
    else:
        symbol = '÷'
        result = int(param1) / int(param2)
    context = {
            'param1': param1,
            'param2': param2,
            'symbol': symbol,
            'result': result
        }
    return render(request, 'multi_output3.html', context)


class MyAppFormView(generic.FormView):
    template_name = 'form01.html'
    form_class = MyAppForm
    success_url = reverse_lazy('my_app:form01')
