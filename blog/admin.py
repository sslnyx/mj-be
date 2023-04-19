from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_date')

    # def author_name(self, obj):
    #     return obj.author.username
    # author_name.short_description = 'Author'
