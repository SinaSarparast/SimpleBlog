from django import forms
from froala_editor.widgets import FroalaEditor

class NameForm(forms.Form):
    title = forms.CharField(label='Title', max_length=30)
    summary = forms.CharField(label='Summary', max_length=300)
    tags = forms.CharField(label='tags', max_length=30)
    # content = forms.TextInput(attrs={'required': True,'size': 3000})
    content = forms.CharField(widget=FroalaEditor)
