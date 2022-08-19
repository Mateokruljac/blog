from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from .models import Category, Comment, Post
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
    
        
    # get_context_data nam omogućuje da se "catergoy" konstantno pojavljuje na strancima
    #na kojima smo stavili ovu metodu....pojavljuje se u obliku rječnika 
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context
                
        
class ArticalDetailView(DetailView):
    model = Post
    template_name = "detail.html"

    
    # štp ćemo dobiti ako uključimo detalje stranice ???    
    def get_context_data(self, *args, **kwargs):
        # početak je identičamn
        category_menu = Category.objects.all()
        context = super(ArticalDetailView,self).get_context_data(*args, **kwargs)
        #provjeravamo postoji li post, ukoliko ne postoji vratit će nam error 404
        # bitan je id je pomoću njega znamo 
        valid_post = get_object_or_404(Post,id = self.kwargs["pk"])
        #ukoliko je post validan provjeravamo koliko je puta netko lajako post
        total_likes = valid_post.total_likes()
        #like u početku ne postoji ali ako ga netko stisne bit će postojan
        liked = False
        if valid_post.like.filter(id = self.request.user.id).exists():
           liked = True    
        #da ovoj će stranici biti prikazani kateogrije,lajkovi i broj lajkova
        context["total_likes"] = total_likes
        context["category_menu"] = category_menu
        context["liked"] = liked
        return context

class AddPostView(CreateView): 
    model = Post
    form_class = PostForm
    template_name  = "add_post.html"
    success_url = reverse_lazy("success_addpost")
    # fields = "__all__"

        
    # get_context_data nam omogućuje da se "catergoy" konstantno pojavljuje na strancima
    #na kojima smo stavili ovu metodu....pojavljuje se u obliku rječnika 
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddPostView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

def success_add_post(request):
    return render (request,"success_add_post.html",{})

class AddCategoryView(CreateView): 
    model = Category
    template_name  = "add_category.html"
    fields = "__all__"
    success_url = reverse_lazy("success_category")
        
    # get_context_data nam omogućuje da se "catergoy" konstantno pojavljuje na strancima
    #na kojima smo stavili ovu metodu....pojavljuje se u obliku rječnika 
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddCategoryView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

def success_addcategory(request):
    category = Category.objects.all().order_by("-id")[0]
    return render (request, "success_category.html",{"category":category})

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm # koristiti ili from_class ili fields ne može oboje
    # fields = ["title","title_tag","body"]
    template_name = "update_post.html"
    
    # get_context_data nam omogućuje da se "catergoy" konstantno pojavljuje na strancima
    #na kojima smo stavili ovu metodu....pojavljuje se u obliku rječnika 
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(UpdatePostView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 

class DeletePostView(DeleteView):
    model = Post
    form_class = PostForm
    template_name = "delete_post.html"
    #nakon što smo obrisali post vraća nas na home 
    #reverse_lazy najčešće korstimo kod generic.based klasa 
    success_url = reverse_lazy("home")
    
         
    # get_context_data nam omogućuje da se "catergoy" konstantno pojavljuje na strancima
    #na kojima smo stavili ovu metodu....pojavljuje se u obliku rječnika 
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(DeletePostView,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context
    
def CategoryView(requests,category):
        # razlog replace() je pokušaj slugiranja
        #filtrira traženu kategoriju
        category_post  = Post.objects.filter(category = category.replace("-"," "))
        return render(requests,"category.html",{"category":category.title().replace("-"," "),"category_post" : category_post})
    
def LikeView (request,id):
    #da bismo mogli lajkati moramo provjeriti postoji li post uopće korsneći get or 404 
    
    post = get_object_or_404(Post,id = request.POST["like_post"])
    # u početku lajka nema
    liked = False
    #ako je user već lajkao i opet stisne onda će dislikati
    if post.like.filter(id = request.user.id).exists():
        #usera brišemo iz total_Like te like postaje False
        post.like.remove(request.user)
        liked = False
        return HttpResponseRedirect(reverse('artical_detail',args = ([str(id)])))
    else:    
        #obrnuta radnja 
        post.like.add(request.user)
        liked = True
        return HttpResponseRedirect(reverse('artical_detail',args = ([str(id)])))

#dodati komentar    
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    ordering = ["- date_time"]
    #ako je forma ispravna sačuva se komentar
    def form_valid(self,form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)
    #vraća nam home 
    success_url = reverse_lazy("home")

