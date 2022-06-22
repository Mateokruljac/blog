from django.urls import path
from .views import AddCommentView, CategoryView, ArticalDetailView, HomeView,AddPostView,UpdatePostView, DeletePostView,AddCategoryView,LikeView

urlpatterns = [
    path('',HomeView.as_view(),name ="home"),
    path('artical_detail/<int:pk>',ArticalDetailView.as_view(),name="artical_detail"),
    path('add_post/',AddPostView.as_view(),name = "add_post"),
    path('edit_post/<int:pk>',UpdatePostView.as_view(),name = "edit_post"),
    path('delete_post/<int:pk>',DeletePostView.as_view(),name = "delete_post"),
    path('add_category',AddCategoryView.as_view(),name = "add_category"),
    path('category/<str:category>',CategoryView,name = "category"),
    path('like_post/<int:id>',LikeView,name = "like_post"),
    path('aritcle/<int:pk>/add_comment',AddCommentView.as_view(),name ="add_comment")


  
]