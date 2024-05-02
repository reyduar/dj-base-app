from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from pages.forms import SearchForm
from .models import Page

# Create your views here.
class PagesListView(ListView):
    model = Page

class PagesDetailView(DetailView):
    model = Page

class PagesSearchView(TemplateView):
     template_name = "pages/page_form.html"
     model = Page
     def get(self, request, *args, **kwargs):
        list_results = Page.objects.all()
        form = SearchForm()
        return render(request, self.template_name, {'form': form, 'pages': list_results})
     
     def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data['search']
            results = Page.objects.filter(title__icontains=keywords)
            list_results = results

        return render(request, self.template_name, {'form': form, 'keywords': keywords, 'pages': list_results})
     

