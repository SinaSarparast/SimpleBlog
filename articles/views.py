from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import NameForm, ArticleForm
from .models import Post, Tag, Category, ArticleAuthor
from django.utils.text import slugify
from django.views.decorators.http import require_http_methods
from django.http import Http404
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


def index(request):
    return HttpResponse("Hello, world. You're at the articles index.")


#LoginRequiredMixin is required for user authentication
class ArticleCreate(LoginRequiredMixin,CreateView):
    template_name = 'articles/article_form.html'
    model = Post
    # fields = ['title','summary','content']
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        article   =   form.save(commit=False)
        article.slug = slugify(article.title)
        article.full_clean()
        return super().form_valid(form)


class ReadView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    template_name = 'articles/article.html'
    model = Post


class Update(UpdateView):
    model   =   Post
    template_name   =   'articles/article_form.html'
    form_class  =   ArticleForm


def delete_article(request, slug):
    try:
        article = Post.objects.get(id= 5)
        article.delete()
        return render("<h1>Successfully deleted!</h1>")
    except Post.DoesNotExist:
        raise Http404("No such a article found! Can not complete the delete operation.")
