from django.contrib import admin
from deejango.blog.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'author', 'created')
	search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'created')
	search_fields = ['author']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)