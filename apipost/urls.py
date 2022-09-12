from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    #path('', PostListView.as_view(), name='blog-home'),

]
