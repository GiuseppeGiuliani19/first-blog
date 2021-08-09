from django.urls import path
from . import views


urlpatterns = [
    path('', views.recipes_view, name='post_list'),
    path('search', views.search, name='search'),
   # path('ip', views.ip_data, name='ip_data'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    #errore per la parola hack
    path('errore/', views.post_new, name='post_new'),
]