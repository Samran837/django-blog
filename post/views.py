from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (ListView,
                                   DetailView,
                                     CreateView,
                                       UpdateView,
                                         DeleteView)


from django.contrib.auth.models import User
from django.core.paginator import Paginator


posts = [
    {
       'author' : 'coreyos' ,
       'title' : 'Blog post 1',
       'content' : 'First post content' ,
       'date_posted' : 'February 11 2026' 
    } ,
     {
       'author' : 'jane doe' ,
       'title' : 'Blog post 2',
       'content' : 'second post content' ,
       'date_posted' : 'February 12 2026'
    }
] 

def user_posts(request, user_id):
    user = User.objects.get(id=user_id)  # Get the user by ID
    post_list = Post.objects.filter(auther=user)  # Filter posts by the specified user
    paginator = Paginator(post_list, 10)  # 10 posts per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the current page of posts
    
    return render(request, 'youstupid/userauthor.html', {'page_obj': page_obj, 'user': user})




def home (request) :
    context = {
        'posts' : Post.objects.all()
    }
    return render(request , 'youstupid/home.html' , context)


class PostListView(ListView) : # <app>/<model>_<viewtype>.html
    model = Post
    template_name = 'youstupid/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class PostDetailView(DetailView) :
    model = Post   
    template_name = 'youstupid/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView) :
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form) :
        form.instance.auther = self.request.user
        return super().form_valid(form)   
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView) :
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form) :
        form.instance.auther = self.request.user
        return super().form_valid(form)

    def test_func(self) :
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView) :
    model = Post
    success_url = '/'

    def test_func(self) :
        post = self.get_object()
        if self.request.user == post.auther:
            return True
        return False


def about(request) :
    return render(request , 'youstupid/about.html' , {'title' : 'About'})






