from django import forms

class FirstForm(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    # dodanie odpowiedniego widgetu do htmla
