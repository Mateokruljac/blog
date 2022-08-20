from django import forms
from .models import Comment, Post,Category
from django.contrib.auth.models import User

choices = Category.objects.all().values_list("name","name")#uvijek moramo dvaput navest prvi put je naredba drugi izvršavanje
choices_list = []



for item in choices:
    choices_list.append(item)
class PostForm(forms.ModelForm): # greška je ako stavimo form bez model 
    class Meta:
        model  = Post
        fields = ["title","title_tag","body","category","snippet","image"]   
        widgets = {
            "body": forms.Textarea(attrs={"class":"form-control","placeholder":"Write..."}),
           

        }
       
    
    def __init__(self,*args, **kwargs):
        super(PostForm,self).__init__(*args, **kwargs)

        self.fields["title"] = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}))
        self.fields["title_tag"] = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Tag..."}))
        self.fields["snippet"] = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",}))
 
        self.fields["category"] = forms.CharField(widget=forms.Select(choices = choices_list,attrs={"class":"form-control",
                                                                                                    "placeholder":"Choice"}))                                                                                                
       

class EditForm(forms.ModelForm): # greška je ako stavimo form bez model 
    class Meta:
        model  = Post
        fields = ["title","title_tag","body","category","snippet","image"]
        widgets = {
            "body": forms.Textarea(attrs={"class":"form-control","placeholder":"Write..."}),
            "author" : forms.Select(attrs= {"class":"form-control","id":"requestUser"})
            

        }
       
    
    def __init__(self,*args, **kwargs):
        super(EditForm,self).__init__(*args, **kwargs)
        self.fields["title"] = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}))
        self.fields["title_tag"] = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Tag..."}))
        self.fields["snippet"] = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",}))
        self.fields["category"] = forms.CharField(widget=forms.Select(choices = choices_list,attrs={"class":"form-control",
                                                                                                    "placeholder":"Choice"}))
       
        
        
class CommentForm(forms.ModelForm):
     class Meta:
        model  = Comment
        fields = ["name","body"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control","placeholder":"Name"}),
            "body" :  forms.Textarea(attrs={"class":"form-control","placeholder":"Write..."}),
        }
        