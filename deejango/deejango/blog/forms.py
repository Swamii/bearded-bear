from django import forms
from deejango.blog.models import Comment

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ['post', 'author']