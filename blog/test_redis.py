from .models import Post


def get_recipes():
    posts = list(Post.objects.filter().order_by('-created_date'))
    return posts

