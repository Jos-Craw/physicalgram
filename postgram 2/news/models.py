from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import Signal
from .utilities import send_activation_notification
import os


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True,
                                       verbose_name='Прошел активацию?')
    avatar = models.ImageField(null=True, blank=True, upload_to="image/profile/")

    class Meta(AbstractUser.Meta):
        pass


class Post(models.Model):
    content = models.TextField(null=True, blank=False)
    image = models.ImageField(upload_to='image/%Y/%m/%d/',blank=True,null=True)
    file = models.FileField(upload_to='files/%Y/%m/%d/',blank=True,null=True)
    video = models.FileField(upload_to='video/%Y/%m/%d/',blank=True,null=True)
    audio = models.FileField(upload_to='audio/%Y/%m/%d/',blank=True,null=True)
    author = models.ForeignKey(AdvUser, on_delete=models.CASCADE, null=True)
    pubdate = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Publication date')

    class Meta:
        verbose_name_plural = 'Posts'
        verbose_name = 'Post'
        ordering = ['-pubdate']

    def filename(self):
        return os.path.basename(self.file.name)


class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
	content = models.TextField(null=True, blank=False)
	author = models.CharField(max_length=30)
	pubdate = models.DateTimeField(auto_now_add=True, db_index=True)
	image = models.ImageField(upload_to='image/%Y/%m/%d/',blank=True,null=True)
	file = models.FileField(upload_to='files/%Y/%m/%d/',blank=True,null=True)
	video = models.FileField(upload_to='video/%Y/%m/%d/',blank=True,null=True)
	audio = models.FileField(upload_to='audio/%Y/%m/%d/',blank=True,null=True)

	class Meta:
		verbose_name_plural = 'Comments'
		verbose_name = 'Comment'
		ordering = ['pubdate']


user_registrated = Signal(['instance'])


def user_registrated_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registrated.connect(user_registrated_dispatcher)
