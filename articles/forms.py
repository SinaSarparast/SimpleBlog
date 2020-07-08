from django import forms
from .models import Tag, Post
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField

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
        widget  = CKEditorUploadingWidget(config_name='default')
        # label   =   'متن'
        )
    # content = RichTextUploadingField()
    title =   forms.CharField(
        label   =   'عنوان',
        initial =   _('Article\'s Title')
        )
    class Meta:
        model = Post
        # fields = '__all__'

        fields = ['title','content']
        labels = {
            'summary': 'خلاصه'
        }
        help_texts = {
            'content': 'متن مقاله'
        }
        error_messages = {
            'NON_FIELD_ERRORS': {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique."
            }
        }
