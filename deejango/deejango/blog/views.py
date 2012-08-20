from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from deejango.blog.models import Post

def posts_all(request):
	posts = Post.objects.all().order_by('-created')
	paginator = Paginator(posts, 2)
	page = request.GET.get('page')

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts': posts}

	return render_to_response('blog.html', context, RequestContext(request))

def specific_post(request, postslug):
	post = Post.objects.get(slug=postslug)
	context = {'post': post}
	return render_to_response('specific_post.html', context, RequestContext(request))