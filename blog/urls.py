from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHome.as_view(), name='blog_home'),
    path('create', views.Create.as_view(), name='create'),
    path('<int:pk>', views.PostDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='blog-delete'),
]
