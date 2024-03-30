from django.shortcuts import render

# Create your views here.


from django.views.generic import TemplateView,CreateView,FormView,View,UpdateView,DetailView

class HomePageView(TemplateView):
    template_name = 'index.html'