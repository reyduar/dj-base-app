from django.forms import ModelForm

from pages.models import Search

class SearchForm(ModelForm):
    class Meta:
        model = Search
        fields = ['keywords']
        labels = {
            'keywords': 'Palabras clave'
        }
    