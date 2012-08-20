from django.shortcuts import render_to_response
from django.template import RequestContext
from deejango.blog.models import Post

def posts_all(request):
	post = Post.objects.all().order_by('-created')
	context = {'post': post}

	return render_to_response('blog.html', context, RequestContext(request))

def specific_post(request, postslug):
	post = Post.objects.get(slug=postslug)
	context = {'post': post}
	return render_to_response('specific_post.html', context, RequestContext(request))