from django import forms

class SearchForm(forms.Form):
    search_str = forms.CharField(label='search:', max_length=100)