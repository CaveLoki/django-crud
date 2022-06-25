from pyexpat import model
from django.shortcuts import render
from .models import Post

# Create your views here.
class PostListView(ListView):
    model : Post 

class PostDetailView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog : all")

class PostDetailView(PostDetailView):
    model = Post

class PostUpdateView(UpateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

    









