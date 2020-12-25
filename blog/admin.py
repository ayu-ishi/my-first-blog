from django.contrib import admin
from .models import Post

# Register your models here.
#postを引数に渡す
admin.site.register(Post)