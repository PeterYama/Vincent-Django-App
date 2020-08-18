from django.shortcuts import render
from django.views.generic import ListView
from .models import PostsModel

class HomePageView(ListView):   
    model = PostsModel
    template_name = 'home.html'