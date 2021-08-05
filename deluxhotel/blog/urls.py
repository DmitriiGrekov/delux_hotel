from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostListTagsView)

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
    path('tags/<int:pk>/', PostListTagsView.as_view(), name='tags_view'),
]
