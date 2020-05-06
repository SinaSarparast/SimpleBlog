from django import forms
from froala_editor.widgets import FroalaEditor
from .models import Tag, Category, Post
from django.forms import ModelForm

class NameForm(forms.Form):
    title   =   forms.CharField(label='عنوان مقاله', max_length=30)
    summary =   forms.CharField(label='چکیده مقاله', max_length=400)
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


class ArticleForm(ModelForm):
    content =   forms.CharField(
        widget  =   FroalaEditor,
        label   =   'متن'
        )
    category=   forms.ModelChoiceField(
        queryset =   Category.objects.all(),
        label   =   'دسته'
        )
    class Meta:
        model = Post
        # fields = '__all__'

        fields = ['title','summary','category','content']
        labels = {
            'title': 'عنوان',
            'summary': 'خلاصه'
        }
        help_texts = {
            'title': 'عنوان مقاله',
            'summary': 'خلاصه مقاله',
            'category': 'دسته مقاله',
            'content': 'متن مقاله',
        }
        error_messages = {
            'NON_FIELD_ERRORS': {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique."
            }
        }
