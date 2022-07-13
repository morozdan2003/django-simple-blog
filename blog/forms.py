from django import forms

class PostWriteForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}))
    contents = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control form-control-lg"}))