from django.shortcuts import render
from .models import Post, Like
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.dispatch import receiver
from django.contrib.auth.decorators import permission_required
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
import ipapi
from django.conf import settings
from .test_redis import get_recipes
from django.urls import reverse

def tutorial(request):
    return render(request, 'blog/tutorial.html')

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
@cache_page(CACHE_TTL)
def recipes_view(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')

        post_obj = Post.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

    return render(request, 'blog/post_list.html', {
        'posts': get_recipes()
    })

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_title = Post.objects.filter(title__contains=searched).order_by('-created_date')


        return render(request, 'blog/search.html',
                      {
                      'search_title': search_title,
                       'searched': searched
                      })
    else:
        return render(request, 'blog/search.html', {'posts': get_recipes()})
@cache_page(CACHE_TTL)
def ip(request):
    search = request.POST.get('search')
    data = ipapi.location(ip=search, output='json')
    return render(request, 'blog/ip.html', {'data': data})

#in questa funzione vengono inserite tutte le transazioni per ogni post
def writeOnchain(request):
    newPost = []
    posts = Post.objects.filter()
    for post in posts:
        if post.hash == None and post.TxId == None:
                post.writeOnchain()
        else:
                newPost.append(
                    {
                        'title': post.title,
                        'hash': post.hash,
                        'TxId': post.TxId
                    }
                )
    return JsonResponse(newPost, safe=False)

#post dell'ultima ora
def posts(request):
    response = []
    posts = Post.objects.filter().order_by('-created_date')
    for post in posts:
        if post.created_date >= timezone.now() - datetime.timedelta(hours=1):
            response.append(
                {
                    'published_date': post.created_date,
                    'title': post.title,
                    'text': post.text,
                    'author': f"{post.author}",
                    'hash': post.hash,
                    'TxId': post.TxId
                }
            )
    return JsonResponse(response, safe=False)

#post details
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#funzione per effettuare un nuovo post,i post non possono contenere 'hack'
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                #post.published_date = timezone.now()
                if 'hack' not in post.text:
                    post.save()
                    return redirect('post_detail', pk=post.pk)
                else:
                    return render(request, 'blog/errore.html')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
#editor post
@login_required
def post_edit(request, pk):
    users = User.objects.all()
    post = get_object_or_404(Post, pk=pk)
    for user in users:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)

            if form.is_valid() and 'hack' not in post.text:
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
            else:
                return render(request, 'blog/errore_hack.html')
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
#view inerente alla registrazione,inserisco delle variabili che mi facciano restituire l'ip attuale,non sono riuscito a trovare l'ultimo
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = RegisterForm()
    return render(request, "blog/register.html", {"form": form, 'posts': posts})


#lista_bozza
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
#posts pubblicated
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
#remove
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
#id user
def id_utente(request):
    return render(request, 'blog/id_utente.html')

def list_specific_user(request):
    users = User.objects.all()
    response = []
    for user in users:
        if user.is_active == True:
                    for user in users:

                                    response.append(
                                        {
                                            user.username: len(Post.objects.filter(author=user))
                                        }
                                    )

                    return HttpResponse(response)
        else:
            return render(request, 'blog/errore_list_specificuser.html')

#view per vedere quante volte una stringa è contenuta nei vari posts
def string(response):
    posts = Post.objects.all()
    list_post = []
    for post in posts:
        if "post" in post.text:
            list_post.append(post.text)
    return HttpResponse(f'<h1>La parola "post" è contenuta in :{len(list_post)} posts</h1>')




















