from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy

from . import models

# Propose list view
#-------------------
class ProposeView(ListView):

    model = models.Propose
    template_name = 'base.html'

# Projector create view
#-------------------
class ProposeCreateView(CreateView):

    model = models.Propose
    template_name = 'form.html'
    success_url = reverse_lazy('poll:propose-list')
    fields = ['name', 'propost']

# Projector edit
#-------------------
class ProposeDetailView(UpdateView):

    model = models.Propose
    template_name = 'detail.html'
    fields = ['up', 'down']


    def get_context_data(self, **kwargs):
        kwargs['comment'] = models.Comment.objects.all()

        return super(ProposeDetailView, self).get_context_data(**kwargs)

    def get_queryset(self):
        return models.Propose.objects.all()
