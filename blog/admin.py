from django.contrib import admin
from .models import Post, Like

class PostAdmin(admin.ModelAdmin):
    list_display = ["__str__", "published_date"]
    list_filter = ["published_date", "author"]
    search_fields = ["title", "text"]

    class Meta:
        model = Post



admin.site.register(Post, PostAdmin)
admin.site.register(Like)