from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('post/<int:user_id>/<slug:slug>/', views.PostDetailView.as_view(), name="post_detail"),
    path('post/delete/<int:post_id>/', views.PostDeleteView.as_view(), name="post_delete"),
    path('post/update/<int:post_id>/', views.PostUpdateView.as_view(), name="post_update"),
    path('post/create/', views.PostCreateView.as_view(), name="post_create"),
    path('reply/<int:post_id>/<int:comment_id>', views.CommentAddReplyView.as_view(), name="reply_comment"),
    path('like/<int:post_id>', views.PostLikeView.as_view(), name="post_like")
]
