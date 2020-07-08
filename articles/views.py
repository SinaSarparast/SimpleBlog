from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import ArticleForm
from .models import Post, Tag, ArticleAuthor
from django.utils.text import slugify
from django.views.decorators.http import require_http_methods
from django.http import Http404
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

class ArticleListView(ListView):
    template_name = 'articles/home.html'
    model = Post
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ReadView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    template_name = 'articles/article.html'
    model = Post


#LoginRequiredMixin is required for user authentication
class AddView(LoginRequiredMixin,CreateView):
    template_name = 'articles/article_form.html'
    model = Post
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        article   =   form.save(commit=False)

        article.slug = slugify(article.title,allow_unicode=True)
        print(20*"*")
        print(article.slug)
        article.full_clean()
        return super().form_valid(form)


class EdithView(LoginRequiredMixin,UpdateView):
    model   =   Post
    template_name   =   'articles/article_form.html'
    form_class  =   ArticleForm


class DeleteView(LoginRequiredMixin,DeleteView):
    model   =   Post
    template_name   =   'articles/article_form.html'
    form_class  =   ArticleForm
    success_url = reverse_lazy('article-list')
