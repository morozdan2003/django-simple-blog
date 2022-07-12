from django.contrib import admin
from .models import Post

# settings for displaying the model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_at')

# register post objects in admin site
admin.site.register(Post, PostAdmin)