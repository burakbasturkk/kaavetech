from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Category (models.Model):
    name = models.CharField (max_length=150)
    mail = models.EmailField(max_length=254, default="mail")
    telefon = models.CharField(null=False, blank=False, unique=True, max_length=11, default="telefon")
    adres = models.CharField (max_length=150, default="adres", blank=True)
    slug = models.SlugField(null=False, blank=True,unique=True, db_index=True,editable=False)
    #slug = AutoSlugField(populate_from ='name', always_update = True,)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



    def __str__(self) :
        return self.name


class Blog (models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
   # slug = AutoSlugField(populate_from ='title', always_update = True,)
    categories = models.ForeignKey(Category, null=True,blank=True, on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
