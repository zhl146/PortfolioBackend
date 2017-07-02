from django.db import models
from django.utils.text import slugify
from html.parser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


'''import hashlib'''


class User(models.Model):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return self.last_name + ", " + self.first_name + " (" + self.username + ")"

    '''def save(self, *args, **kwargs):
        self.password = hashlib.sha224(self.password.encode('utf-8')).hexdigest()
        super(User, self).save(*args, **kwargs)'''  # This needs to go in a user create procedure


class Tag(models.Model):
    tag_desc = models.CharField(max_length=128)

    def __str__(self):
        return self.tag_desc


class Category(models.Model):
    category_desc = models.CharField(max_length=128)

    def __str__(self):
        return self.category_desc


class Content(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=512, unique=True)
    slug = models.SlugField(blank=True, null=True, default=None, unique=True)
    content = models.TextField()
    tag_list = models.ManyToManyField(Tag)

    def __str__(self):
        return self.author.last_name + ", " + self.author.first_name + ": " + self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        else:
            self.slug = slugify(self.slug)
        super(Content, self).save(*args, **kwargs)

    def get_post_json(self):
        client_json = self.get_content_meta()
        client_json['content'] = self.content
        return client_json

    def get_summary_json(self):
        client_json = self.get_content_meta()
        client_json['content'] = self.summary()
        return client_json

    def get_content_meta(self):
        tag_list = []
        for tag in self.tag_list.all():
            tag_list.append(tag.tag_desc)
        client_json = {
            'author': self.author.first_name + ' ' + self.author.last_name,
            'title': self.title,
            'tag_list': tag_list,
            'create_date': self.create_date,
            'edit_date': self.edit_date
        }
        return client_json

    def strip_tags(self):
        s = MLStripper()
        s.feed(self.content)
        return s.get_data()

    def summary(self):
        return self.strip_tags().split(' ')
