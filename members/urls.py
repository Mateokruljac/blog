from django.urls import path
from .views import ChangePassword, CreateProfilePage, CreateUserForm, EditUserForm,UserDetailView,UserEditView, about_me,loginview,password_success


urlpatterns = [
    path('register/',CreateUserForm.as_view(),name = "register"),
    path("edit_profile",EditUserForm.as_view(),name = "edit_profile"),
    path("<int:pk>/profile_page",UserDetailView.as_view(),name = "profile_page"),
    path("edit_profile_page/<int:pk>",UserEditView.as_view(),name = "edit_profile_page"),
    path("create_profile_page",CreateProfilePage.as_view(),name ="create_profile_page"),
    path('password_change',ChangePassword.as_view(),name ="password_change"),
    path('success_changed',password_success,name ="success_changed"),
    path('about_me',about_me,name = "about_me"),
    path("loginview/",loginview,name = "loginview")


]
