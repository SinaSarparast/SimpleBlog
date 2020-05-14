from django import forms
from froala_editor.widgets import FroalaEditor
from .models import Tag, Category, Post
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


# # class NameForm(forms.Form): (difference between form.form and modelform)
# Forms created from forms.Form are manually configured by you. You're better off
# using these for forms that do not directly interact with models. For example
# a contact form, or a newsletter subscription form, where you might
# not necessarily be interacting with the database. Where as a form created from
# forms.ModelForm will be automatically created and then can later be
# tweaked by you. The best examples really are from the superb documentation
# provided on the Django website.


class ArticleForm(ModelForm):
    content =   forms.CharField(
        widget  = CKEditorWidget(config_name='awesome_ckeditor')
        # label   =   'متن'
        )
    title =   forms.CharField(
        label   =   'عنوان',
        initial =   _('Article\'s Title')
        )
    category=   forms.ModelChoiceField(
        queryset =   Category.objects.all(),
        label   =   'دسته'
        )
    summary=   forms.CharField(
        widget=forms.Textarea(attrs={'class' : 'article_summary'}),
        label   =   'خلاصه',
        initial =   _('Initial headline')
        )
    class Meta:
        model = Post
        # fields = '__all__'

        fields = ['title','summary','category','content']
        labels = {
            'summary': 'خلاصه'
        }
        help_texts = {
            'category': 'دسته مقاله',
            'content': 'متن مقاله'
        }
        error_messages = {
            'NON_FIELD_ERRORS': {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique."
            }
        }
