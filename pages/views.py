from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django import forms

from pages.forms import SearchForm
from .models import Page

# Create your views here.
class PagesListView(ListView):
    model = Page

class PagesDetailView(DetailView):
    model = Page

class PagesCreateView(FormView):
     template_name = "pages/page_form.html"
     
     
     def get(self, request, *args, **kwargs):
         form = SearchForm()
         print(form.fields.values())
         return render(request, self.template_name, {'form': form})
     def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, self.template_name, {'form': form})
     

