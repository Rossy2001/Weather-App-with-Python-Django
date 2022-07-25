# from django.forms import ModelForm, TextInput
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Search  
class SearchForm(forms.ModelForm):
    address = forms.CharField(label='')

    class Meta:
        model = Search
        fields = ['address', ]