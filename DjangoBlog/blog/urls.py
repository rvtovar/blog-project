from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name="detail"),
    path('post/new/', views.PostCreateView.as_view(), name="create"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path("about/", views.about, name="about")
]
