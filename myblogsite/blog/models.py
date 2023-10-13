from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    f_name = models.CharField(max_length=200)
    f_last = models.CharField(max_length=200)
    roll= models.CharField(max_length=50)

    def __str__(self):
       return  f'{self.f_name} + {self.f_last}'
class Article(models.Model):
    writer = models.CharField(max_length=400)
    title = models. CharField(max_length= 200)
    blog_post = models.TextField(max_length=1200)
    date_pub = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.title} by {self.writer}'

class Comment(models.Model):
    post= models.ForeignKey(Article, on_delete = models.CASCADE, related_name = 'comments',null = True)
    name = models.CharField(max_length=60)
    date_posted = models.DateTimeField( auto_now_add = True)
    body = models.TextField(max_length=400,null = True)
    class Meta:
        ordering = ['date_posted']

    def __str__(self):
       return  f'comment by {self.name}'

    