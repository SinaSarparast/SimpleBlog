from django import forms
from .models import Tag, Post
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor_uploader.fields import RichTextUploadingField

<<<<<<< HEAD
class NameForm(forms.Form):
    title   =   forms.CharField(label='title', max_length=30)
    category=   forms.ModelChoiceField(
        queryset    =   Category.objects.all())
    content =   forms.CharField(widget=FroalaEditor)

    # FBVs must be refactored to CBVs because there is a lot of messy code
    # I need to fix the tags model so that the edith view works!
        # Probably the code below can solve the problem if I fix the queryset
    # tags = forms.ModelChoiceField(
    #     queryset = Tag.objects.values_list("name", flat=True).distinct(),
    #     empty_label=None
    # )
    # tags    =   models.CharField(max_length=3, choices=LOCATIONS)
=======
# # class NameForm(forms.Form): (difference between form.form and modelform)
# Forms created from forms.Form are manually configured by you. You're better off
# using these for forms that do not directly interact with models. For example
# a contact form, or a newsletter subscription form, where you might
# not necessarily be interacting with the database. Where as a form created from
# forms.ModelForm will be automatically created and then can later be
# tweaked by you. The best examples really are from the superb documentation
# provided on the Django website.
>>>>>>> 04734b924d6bf86514447a6be59bb3f0387b342f


class ArticleForm(ModelForm):
    content =   forms.CharField(
<<<<<<< HEAD
        widget  =   FroalaEditor,
        label   =   'content'
        )
    category=   forms.ModelChoiceField(
        queryset =   Category.objects.all(),
        label   =   'category'
=======
        widget  = CKEditorUploadingWidget(config_name='default')
        # label   =   'متن'
        )
    # content = RichTextUploadingField()
    title =   forms.CharField(
        label   =   'Title',
        initial =   _('Article\'s Title')
>>>>>>> 04734b924d6bf86514447a6be59bb3f0387b342f
        )
    class Meta:
        model = Post
        # fields = '__all__'

<<<<<<< HEAD
        fields = ['title','summary','category','content']
=======
        fields = ['title','content']
        labels = {
            'summary': 'summary'
        }
        help_texts = {
            'content': 'content'
        }
>>>>>>> 04734b924d6bf86514447a6be59bb3f0387b342f
        error_messages = {
            'NON_FIELD_ERRORS': {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique."
            }
        }
