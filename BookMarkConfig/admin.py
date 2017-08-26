from django.contrib import admin

# Register your models here.
from BookMarkConfig.models import BookMark
from blog.models import Post


class BookMarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

admin.site.register(BookMark, BookMarkAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date', )
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug' : ('title', )}

admin.site.register(Post, PostAdmin)