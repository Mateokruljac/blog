from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 250)
  
    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url (self):
        return reverse("home")
    
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    biography = models.TextField()
    profile_images = models.ImageField(null = True, blank = True,upload_to = "images/profile")
    facebook_url = models.CharField(null=True,blank = "True", max_length=255)
    instagram_url = models.CharField(null=True,blank = "True", max_length=255)
    twitter_url = models.CharField(null=True,blank = "True", max_length=255)
    linkedin_url = models.CharField(null=True,blank = "True", max_length=255)
    
    def __str__(self):
        return f"User: {self.user}"
    
    def get_absolute_url(self):
        return reverse("home")
    

class Post(models.Model):
    title  = models.CharField(max_length=200)
    title_tag  = models.CharField(max_length=200, default="My blog") 
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # body   = models.TextField()
    body = RichTextField(blank = True, null = True)
    snippet = models.CharField(max_length=250,default="Click link above to read a post!")
    post_date = models.DateField(auto_now_add=True)
    image = models.ImageField(null = True, blank = True,upload_to = "images")
    category = models.CharField(max_length=250,default="Uncategorized")
    like  = models.ManyToManyField(User,related_name= "blog_post") 
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}" 
    
    def get_absolute_url (self):
        return reverse("artical_detail",args = str(self.pk) )
    
    def total_likes (self):
        return self.like.count()
    


class Comment(models.Model):
    #foreign key i onetoone možemo slobodno zvati po potrebi
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment")
    name = models.CharField(max_length=200)
    body = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Name:{self.name}\nDate: {self.date_time}" # prikazat će se u admin području
    
    def get_absolute_url(self):
        return reverse('home')
     
    