from django import forms

class PostWriteForm(forms.Form):
    title = forms.CharField(max_length=100)
    contents = forms.CharField(widget=forms.Textarea)