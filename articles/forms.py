from django import forms
from froala_editor.widgets import FroalaEditor

class NameForm(forms.Form):
    title = forms.CharField(label='عنوان مقاله', max_length=30)
    summary = forms.CharField(label='چکیده مقاله', max_length=400)
    rating = forms.IntegerField(label='امتیاز',required=False)
    content = forms.CharField(widget=FroalaEditor)
    tags = forms.CharField(label='برچسب ها (تگ ها)', max_length=100)
