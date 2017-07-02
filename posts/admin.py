from django.contrib import admin

# Register your models here.

from .models import User
admin.site.register(User)

from .models import Tag
admin.site.register(Tag)

from .models import Category
admin.site.register(Category)

from .models import Content
admin.site.register(Content)