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

def index(request):
    return HttpResponse("Hello, world. You're at the articles index.")


# def create_article(request):
#     if request.method == "Get":
#         # form = NameForm()
#         form = ArticleForm()
#     else:
#         # create a form instance and populate it with data from the request:
#         form = ArticleForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             article =   form.save(commit=False)
#             try:
#                 author = ArticleAuthor.objects.get(user = request.user)
#             except ArticleAuthor.DoesNotExist:
#                 author = ArticleAuthor()
#                 author.user = request.user
#                 author.full_clean()
#
#             article.author  =   author
#             article.slug    =   slugify(article.title)
#             article.save()
#
#     return render(request, 'articles/edith_article.html', {'form': form})

from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


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

# def read_article(request, slug):
#     try:
#         article = get_object_or_404(Post, slug=slug)
#         data_to_send = {
#             'title'     :   article.title,
#             'summary'   :   article.summary,
#             'lastmodiefied_date'    :   article.lastmodiefied_date,
#             'content'   :   article.content,
#             'author'    :   article.author
#         }
#         return render(request,  'articles/article.html', data_to_send)
#     except Post.DoesNotExist:
#         raise Http404("Article does not exist!")


def update_article(request, slug):
    if request.method == "GET":
        print("******************")
        print("Get is executed")
        print("******************")
        try:
            article = Post.objects.filter(slug = slug).values()
            form = ArticleForm(article.first())
        except Post.DoesNotExist:
            raise Http404("No MyModel matches the given query.")
        # return reverse(edith_article,args=["hello-world"])
        return render(request, 'articles/edith_article.html', {'form': form})


    if request.method == "POST":
        print("******************")
        print("POST is executed")
        print("******************")

        # if slug is None:
        #     form = article(request.POST)
        #     slug = slugify(request.POST['title'])
        form = ArticleForm(request.POST)
        if form.is_valid():
            article =   form.save(commit=False)
            try:
                author = ArticleAuthor.objects.get(user = request.user)
            except ArticleAuthor.DoesNotExist:
                author = ArticleAuthor()
                author.user = request.user
                author.full_clean()

            article.author  =   author
            article.slug    =   slugify(article.title)
            article.save()

            return HttpResponse("Operation successful!")
            # try:
            #     print(slug)
            #     article     =   Post.objects.filter(slug = slug).update(
            #         title   =   form.cleaned_data['title'],
            #         slug    =   slugify(form.cleaned_data['title'],allow_unicode=True),
            #         # author  =   request.user,
            #         summary =   form.cleaned_data['summary'],
            #         content =   form.cleaned_data['content']
            #         # ,tag     =   form.cleaned_data['tags']
            #         )
            #     print("record updated")
            # except Post.DoesNotExist:
            #     #you have to place dberror here this is just a place holder
            #     # here you can check the type, etc of the error
            #     # messages.error(request, "Database Error ...blah blah %s" % str(dberr))
            #     raise Http404("No post matches the given query.")

        # print('reverse')
        # return render(request, 'articles/edith_article.html', {'form': form})
    # return reverse(edith_article,args=["hello-world"])
    print("******************")
    print("Post is not executed")
    print("******************")
    return render(request, 'articles/edith_article.html', {'form': form})


def delete_article(request, slug):
    try:
        article = Post.objects.get(id= 5)
        article.delete()
        return render("<h1>Successfully deleted!</h1>")
    except Post.DoesNotExist:
        raise Http404("No such a article found! Can not complete the delete operation.")
