"""
Archivo para la configuración de las URLs de la app blog.
"""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns =[
    # path('', views.home, name='home'),
    path('', views.HomeView.as_view(), name='home'),
    path('all/', views.PostList.as_view(), name='post-list'),
    path('by_tag/<slug:tag_slug>', views.PostList.as_view(), name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    # path('create/', views.post_create_view, name='post-create'),
]
