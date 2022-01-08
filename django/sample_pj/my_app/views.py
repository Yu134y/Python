from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse


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
