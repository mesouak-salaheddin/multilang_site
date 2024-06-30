from django.urls import path # type: ignore
from posts.views import BlogHome, BlogPostCreate, BlogPostUpdate, BlogPostDetail, BlogPostDelete

app_name = "posts"

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('nouveau/', BlogPostCreate.as_view(), name='create'),
    path('<str:slug>/', BlogPostDetail.as_view(), name='post_detail'),
    path('edit/<str:slug>/', BlogPostUpdate.as_view(), name='update'),
    path('supprimer/<str:slug>/', BlogPostDelete.as_view(), name='remove'),
]
