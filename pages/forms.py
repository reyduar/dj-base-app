from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)

    def clean_search(self):
        search = self.cleaned_data['search']
        if len(search) < 3:
            raise forms.ValidationError('La busqueda debe contener al menos 3 caracteres')
        return search
   