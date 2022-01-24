from typing import List
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Article


class IndexView(ListView):

    template_name = 'index.html'
    queryset = Article.objects.filter(is_published=True).order_by('-created')[:6]
    context_object_name = 'articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        popular_article = Article.objects.filter(is_published=True).values('uuid', 'title').order_by('-views')[:5]
        context['popular_article'] = popular_article
        return context

index = IndexView.as_view()


# Articleの一覧ページ
class ArticleListView(ListView):

    template_name = 'article/list.html'
    queryset = Article.objects.filter(is_published=True).order_by('-created')
    context_object_name = 'articles'
    paginate_by = 10

article_list = ArticleListView.as_view()


# Articleの詳細ページ
class ArticleDetailView(DetailView):

    template_name = 'article/detail.html'
    queryset = Article.objects.filter(is_published=True)
    context_object_name = 'article'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get(self, request, *args, **kwargs):
        get = super().get(request, *args, **kwargs)
        context = get.context_data

        # incremment views
        article = self.object
        article.views += 1
        article.save()

        recommend = Article.objects.filter(is_published=True).order_by('views').last()
        context['recommend'] = recommend

        return get

article_detail = ArticleDetailView.as_view()