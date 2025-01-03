from django.contrib import admin
from .models import Profile
from .models import Post
from .models import Message,Like
# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Like)