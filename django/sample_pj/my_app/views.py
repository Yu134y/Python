from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from my_app.forms import MyAppForm, MyAppForm2, ProductModelForm
from my_app.models import Product


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


class MyAppFormView2(generic.FormView):
    template_name = 'form02.html'
    form_class = MyAppForm2

    def form_valid(self, form):
        param1 = form.cleaned_data['param1']
        param2 = form.cleaned_data['param2']
        operator = form.cleaned_data['operator']
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
            'form': form,
            'param1': param1,
            'param2': param2,
            'symbol': symbol,
            'result': result
        }
        return render(self.request, self.template_name, context)


class ProductListView(generic.ListView):
    template_name = 'product_list.html'
    model = Product


class ProductDetailView(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product


class ProductCreateView(generic.CreateView):
    template_name = 'product_create.html'
    model = Product
    # fields = ('name', 'price', 'release_date')
    form_class = ProductModelForm
    success_url = reverse_lazy('my_app:product_all')


class ProductUpdateView(generic.UpdateView):
    template_name = 'product_update.html'
    model = Product
    # fields = ('name', 'price', 'release_date')
    form_class = ProductModelForm

    def get_success_url(self):
        return reverse_lazy('my_app:product_detail', kwargs={'pk':self.object.id})


class ProductDeleteView(generic.DeleteView):
    template_name = 'product_delete.html'
    model = Product
    success_url = reverse_lazy('my_app:product_all')
