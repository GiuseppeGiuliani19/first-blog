from django.conf import settings
from django.db import models
from django.utils import timezone
from django.conf import settings
from web3 import Web3
from .utils import sendTransaction
import hashlib
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    liked = models.ManyToManyField(User,
    default=None, blank=True, related_name='liked')
    hash = models.CharField(max_length=66, default=None, null=True)
    TxId = models.CharField(max_length=66, default=None, null=True)


    @property
    def num_likes(self):
        return self.liked.all().count()

    def writeOnchain(self):
        self.hash = hashlib.sha256(self.text.encode('utf-8')).hexdigest()
        self.TxId = sendTransaction(self.hash)
        self.save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

LIKE_CHOICES = (
    ('Like', 'like'),
    ('Unlike', 'unlike'),
)
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)




