from django.contrib import admin
from .models import SocialPost, Image, SocialComment

admin.site.register(SocialPost)
admin.site.register(SocialComment)
admin.site.register(Image)
# Register your models here.
