from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from .models import Category, Comment, Post, Profile
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import CommentForm, EditForm, PostForm
from django.http import HttpResponseRedirect
# Create your views here.
#ListViews - omogućuje rad s listama i vraća nam liste
# DetailView samo detalj


class HomeView(ListView): # na home stranici nam vraća listu
    #koji model i template želimo koristiti
    model = Post 
    template_name = "home.html"
    #možemo proslijediti id da ide od posljednjeg ili nešto drugho npr title, a ako želimo obrnuto stavimo minus
    # najčešće se radi order by date
    ordering = ["title"]
    # ordering = ["-post_date"]
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context
                
        
class ArticalDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticalDetailView,self).get_context_data(*args, **kwargs)
        
        valid_post = get_object_or_404(Post,id = self.kwargs["pk"])
        total_likes = valid_post.total_likes()
        
        liked = False
        if valid_post.like.filter(id = self.request.user.id).exists():
           liked = True    
        
        context["total_likes"] = total_likes
        context["category_menu"] = category_menu
        context["liked"] = liked
        return context

class AddPostView(CreateView): 
    model = Post
    form_class = PostForm
    template_name  = "add_post.html"
    # fields = "__all__"
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddPostView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class AddCategoryView(CreateView): 
    model = Category
    template_name  = "add_category.html"
    fields = "__all__"
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddCategoryView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm # koristiti ili from_class ili fields ne može oboje
    # fields = ["title","title_tag","body"]
    template_name = "update_post.html"
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(UpdatePostView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 

class DeletePostView(DeleteView):
    model = Post
    form_class = PostForm
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
     
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(DeletePostView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context
    
def CategoryView(requests,category):
    
        category_post  = Post.objects.filter(category = category.replace("-"," "))
        print(category_post)
        return render(requests,"category.html",{"category":category.title().replace("-"," "),"category_post" : category_post})
    
def LikeView (request,id):
    post = get_object_or_404(Post,id = request.POST["like_post"])
    liked = False
    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
        liked = False
        return HttpResponseRedirect(reverse('artical_detail',args = ([str(id)])))
    else:    
        post.like.add(request.user)
        liked = True
        return HttpResponseRedirect(reverse('artical_detail',args = ([str(id)])))
    
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    ordering = ["- date_time"]
    def form_valid(self,form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)
    success_url = reverse_lazy("home")



