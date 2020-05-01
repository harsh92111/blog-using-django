from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import post
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

class base(ListView):
    model=post
    template_name='home.html'


class base1(DetailView):
    model=post
    template_name='post_detail.html'

class base2(CreateView):
    model=post
    template_name='post_new.html'
    fields='__all__'

class base3(UpdateView): # new
    model = post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class base4(DeleteView): # new
    model = post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')



# Create your views here.
