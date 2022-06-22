from django import views
from django.urls import path
from .views import CreateProfilePage, CreateUserForm, EditUserForm,UserDetailView,UserEditView, aboutUs, contact


urlpatterns = [
    path('register/',CreateUserForm.as_view(),name = "register"),
    path("edit_profile",EditUserForm.as_view(),name = "edit_profile"),
    path("<int:pk>/profile_page",UserDetailView.as_view(),name = "profile_page"),
    path("<int:pk>/edit_profile_page",UserEditView.as_view(),name = "edit_profile_page"),
    path("create_profile_page",CreateProfilePage.as_view(),name ="create_profile_page"),
    path("about_us",aboutUs,name= "about_us"),
    path("contact",contact,name =  "contact")
         
]