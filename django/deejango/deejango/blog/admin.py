from django.contrib import admin
from deejango.blog.models import Post

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'author', 'created')
	search_fields = ['title']

admin.site.register(Post, PostAdmin)