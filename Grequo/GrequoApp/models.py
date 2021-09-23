from django.db import models
from django.utils import timezone
from django.conf import settings
import uuid

User = settings.AUTH_USER_MODEL


# Create your models here.

class Userquest(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True,
                             serialize=False, verbose_name='ID')
    author = models.ForeignKey(User, default=1,
                               null=False,
                               on_delete=models.CASCADE)
    quest = models.TextField(max_length=300, default='')
    timestamp = models.DateTimeField(default=timezone.now)
    like_count = models.PositiveSmallIntegerField(default=0)
    dislike_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.author.username


class Usercomment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(
        Userquest, null=False, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(
        User, null=False, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return self.comment_author.username

    class Meta:
        ordering = ['timestamp']


class Contactus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default="", max_length=30)
    email = models.EmailField(default="")
    message = models.CharField(default="", max_length=500)

    def __str__(self):
        return self.email


class Likepost(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(
        Userquest, null=False, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, default=1,
                                null=False,
                                on_delete=models.CASCADE)
    is_liked = models.BooleanField(null=True)
    is_disliked = models.BooleanField(null=True)
    # like_count = models.PositiveSmallIntegerField(default=0)
    # dislike_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str(self.post_id.id)
