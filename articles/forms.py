from django import forms
from froala_editor.widgets import FroalaEditor
from .models import Tag, Category, Post

class NameForm(forms.Form):
    title   =   forms.CharField(label='عنوان مقاله', max_length=30)
    summary =   forms.CharField(label='چکیده مقاله', max_length=400)
    category=   forms.ModelChoiceField(
        queryset    =   Category.objects.all())
    # rating  = forms.IntegerField(label='امتیاز',required=False)
    content =   forms.CharField(widget=FroalaEditor)
    # tags    = forms.CharField(label='برچسب ها (تگ ها)', max_length=100)

    # FBVs must be refactored to CBVs because there is a lot of messy code
    # I need to fix the tags model so that the edith view works!
        # Probably the code below can solve the problem if I fix the queryset
    # tags = forms.ModelChoiceField(
    #     queryset = Tag.objects.values_list("name", flat=True).distinct(),
    #     empty_label=None
    # )
    # tags    =   models.CharField(max_length=3, choices=LOCATIONS)

from django.forms import ModelForm

class AuthorForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'title': 'Writer',
        }
        help_texts = {
            'title': 'Article\'s title.',
        }
