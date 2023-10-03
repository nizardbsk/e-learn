from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(null=True,blank=True)
    username=models.CharField(max_length=200)
    avatar=models.ImageField(blank=True,default='avatar.svg')
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.user.username
    @property
    def avatar_url(self):
        try :
            return self.avatar.url
        except:
            return ''
class Tutorial(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    name=models.TextField()
    cover=models.ImageField(blank=True,default='avatar.svg')
    description=models.TextField()
    price=models.IntegerField(blank=True)
    created=models.DateTimeField(auto_now_add=True)
    followers=models.ManyToManyField(Profile,related_name='unrolls')
    @property
    def cover_url(self):
        try :
            return self.cover.url
        except:
            return ''
class Video(models.Model):
    title=models.TextField()
    video=models.FileField(upload_to='videos/', verbose_name="")
    description=models.TextField()
    tutorial=models.ForeignKey(Tutorial,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title + ": " + str(self.video)
    @property
    def video_url(self):
        try :
            return self.video.url
        except:
            return ''
    class Meta:
        ordering = ['created']

class Article(models.Model):
    title=models.TextField()
    text=models.TextField()
    tutorial=models.ForeignKey(Tutorial,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']

class Like(models.Model):
    liker=models.ForeignKey(Profile,on_delete=models.CASCADE)
    tutorial=models.ForeignKey(Tutorial,on_delete=models.CASCADE)

class Comment(models.Model):
    commenter=models.ForeignKey(Profile,on_delete=models.CASCADE)
    tutorial=models.ForeignKey(Tutorial,on_delete=models.CASCADE)
