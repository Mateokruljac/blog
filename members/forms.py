from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
        fields = ["password","first_name","last_name","username","email","date_joined"]
        widgets = {
         "username" : forms.TextInput(attrs = {"class":"form-control"}),
         "date_joined" : forms.DateTimeInput(attrs = {"class":"form-control"}),
        }


class ProfilePageForm(forms.ModelForm):
    instagram_url = forms.CharField(max_length = 200,widget=forms.TextInput(attrs={"class":"form-control"}))
    facebook_url = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    linkeidin_url = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = Profile
        fields = ["biography","profile_images","instagram_url","facebook_url","twitter_url","linkedin_url"]
        
        def __init__(self,*args, **kwargs):
            super(ProfilePageForm,self).__init__(*args, **kwargs)

            self.fields["facebook_url"] = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}))
            self.fields["instagram_url"] = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Tag..."}))
            self.fields["linkedin_url"] = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",}))
    
            
        

            