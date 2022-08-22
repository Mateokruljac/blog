from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm,UserChangeForm
from members.forms import EditForm, EditProfilePage, NewPassword, ProfilePageForm, SignUpForm
from theblog.models import Profile,Category
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render,redirect
from django.contrib import auth, messages

class CreateUserForm(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html" 
    success_url = reverse_lazy("login")
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(CreateUserForm,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class CreateProfilePage(generic.CreateView):
    form_class = ProfilePageForm
    template_name = "registration/create_profile_page.html"

    
    #provjeravamo validaciju trenutnog usera
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form) # čuvamo formu 
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(CreateProfilePage,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 


class EditUserForm(generic.UpdateView):
    form_class =EditForm
    template_name = "registration/edit_profile.html" 
    success_url = reverse_lazy("home")
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(EditUserForm,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 
    

class UserDetailView (generic.DetailView):
    model = Profile
    template_name = "registration/user_profile_page.html"
    
    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(UserDetailView,self).get_context_data(*args, **kwargs)
        user_profile = get_object_or_404(Profile,id = self.kwargs["pk"])
        context["user_profile"] = user_profile 
        category_menu = Category.objects.all()
        context["category_menu"] = category_menu
        
        return context
                

class UserEditView(generic.UpdateView):
    model = Profile
    form_class = EditProfilePage
    template_name = "registration/user_profile_edit.html"
    success_url = reverse_lazy("home")
    
    
    
    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(UserEditView,self).get_context_data(*args, **kwargs)
        user_profile = get_object_or_404(Profile,id = self.kwargs["pk"])
        context["user_profile"] = user_profile 
        category_menu = Category.objects.all()
        context["category_menu"] = category_menu
        
        return context

class ChangePassword(PasswordChangeView):
    form_class = NewPassword
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("success_changed")
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ChangePassword,self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 

def password_success (request):
    return render (request,"registration/success_changed.html",{})



def about_me (request):
    return render(request,"about_me.html",{})


def loginview (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return render (request,"home.html")
        else:
            messages.info(request,"Invalid username or password! Try Again or create new account!")
            return render(request,"registration/login.html")
    else:
        return render (request,"registration/login.html")
            