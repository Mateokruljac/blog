from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm ,UserChangeForm
from django.contrib.auth.models import User
from theblog.models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length = 200,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta: 
        #pogledati kako je name zadan u djangu na način da istražimo stranicu desni klik + ostalo
        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]
        widgets = {
         "username" : forms.TextInput(attrs = {"class":"form-control"}),
        }


class EditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(max_length = 200,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta: 
        #pogledati kako je name zadan u djangu na način da istražimo stranicu desni klik + ostalo
        model = User
        fields = ["first_name","last_name","username","email","date_joined"]
        widgets = {
         "username" : forms.TextInput(attrs = {"class":"form-control"}),
         "date_joined" : forms.DateTimeInput(attrs = {"class":"form-control"}),
        }


class ProfilePageForm(forms.ModelForm):
    instagram_url = forms.CharField(max_length = 200,widget=forms.TextInput(attrs={"class":"form-control"}))
    facebook_url = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    linkedin_url = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Profile
        fields = ["biography","profile_images","instagram_url","facebook_url","twitter_url","linkedin_url"]
        widgets = {
            "biography" : forms.Textarea(attrs = {
                "class" : "form-control",
                "placeholder" : "Write..."
            }),
            "profile_images" : forms.FileInput(attrs = {
                "class" : "form-control"
                }),
            "instagram_url" : forms.TextInput(attrs = {
                "class" : "form-control"
            }),
            "facebook_url" : forms.TextInput(attrs = {
                "class" : "form-control"
            }),
            "twitter_url" : forms.TextInput(attrs = {
                "class" : "form-control"
            }),
            "linkedin_url": forms.TextInput(attrs = {
                "class" : "form-control"
            })
        }
    
            

class EditProfilePage(forms.ModelForm):
    instagram_url = forms.CharField(max_length = 200,widget=forms.TextInput(attrs={"class":"form-control"}))
    facebook_url = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    linkedin_url = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Profile
        fields = ["biography","profile_images","instagram_url","facebook_url","twitter_url","linkedin_url"]
        widgets = {
            "biography" : forms.Textarea(attrs = {
                "class" : "form-control",
                "placeholder" : "Write..."
            }),
            "profile_images" : forms.FileInput(attrs = {
                "class" : "form-control"
                }),
            "instagram_url" : forms.TextInput(attrs = {
                "class" : "form-control"
            }),
            "facebook_url" : forms.TextInput(attrs = {
                "class" : "form-control"
            }),
            "twitter_url" : forms.TextInput(attrs = {
                "class" : "form-control"
            }),
            "linkedin_url": forms.TextInput(attrs = {
                "class" : "form-control"
            })
        }
    
            
       
        
class NewPassword(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs = {
                "class" : "form-control",
            }))
    new_password1 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs = {
                "class" : "form-control",
            }))
    new_password2 = forms.CharField(max_length=100, widget = forms.PasswordInput(attrs = {
                "class" : "form-control",
            }))
    
    class Meta:
        model  = User
        fields = ["old_password","new_password1","new_password2"]
        