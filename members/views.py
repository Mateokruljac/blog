from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from members.forms import EditForm, ProfilePageForm, SignUpForm
from theblog.models import Profile



class CreateUserForm(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html" 
    success_url = reverse_lazy("login")

class CreateProfilePage(generic.CreateView):
    form_class = ProfilePageForm
    template_name = "registration/create_profile_page.html"

    
    #provjeravamo validaciju trenutnog usera
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form) # čuvamo formu 


class EditUserForm(generic.UpdateView):
    form_class =EditForm
    template_name = "registration/edit_profile.html" 
    success_url = reverse_lazy("home")
    
    def get_object(self):
        return self.request.user
    

class UserDetailView (generic.DetailView):
    model = Profile
    template_name = "registration/user_profile_page.html"
    
    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(UserDetailView,self).get_context_data(*args, **kwargs)
        user_profile = get_object_or_404(Profile,id = self.kwargs["pk"])
        context["user_profile"] = user_profile
        return context
                

class UserEditView(generic.UpdateView):
    model = Profile
    template_name = "registration/user_profile_edit.html"
    fields = ["biography","profile_images","facebook_url","instagram_url","linkedin_url","twitter_url"]
    success_url = reverse_lazy("home")
    
    
    
def aboutUs(request):
    return HttpResponse("<h1>Comming Soon</h1>")
    
def contact(request):
    return HttpResponse("<h1>Comming Soon</h1>")