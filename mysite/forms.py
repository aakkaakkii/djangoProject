from django import forms


class NameForm(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    text = forms.CharField(label='text', max_length=500)