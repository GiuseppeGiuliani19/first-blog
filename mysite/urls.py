"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.contrib.auth import views
from blog import views


urlpatterns = [
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('admin/', admin.site.urls),
 #   path('search', views.search, name='search'),
    path('ip', views.ip, name='ip_data'),
    #contiene hash ed identificativi di ogni transazione,la transazione avviene appena creato il post
    path('writeOnchain', views.writeOnchain),
    #url per i posts inseriti nell'ultima ora
    path('posts', views.posts),
    path('', include('blog.urls')),
    #url per la registrazione
    path('register/', views.register, name="register"),
    #url per il login,ho utilizzato una forma crispy che puo essere visualizzata nella pagina html
    path('', include("django.contrib.auth.urls")),
    #url per la una stringa,viene contata quante volte è inserita nei post
    path('string', views.string),
    #quanti sono gli user e quanti post ciascuno ha pubblicato
    path('list_specific_user', views.list_specific_user, name="list_specific_user"),
    path('id', views.id_utente, name='id_utente'),
    path('list_specific_user/', views.list_specific_user, name="list_specific_user")
]
