from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models

# Create your views here.

"""Template View"""
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection'
        return context


"""List View"""
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'school_list.html'


"""Detail View"""
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'school_detail.html'


class SchoolCreateView(CreateView):

    fields = ['name', 'principal', 'location']
    model = models.School
    template_name = 'school_form.html'