from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from deejango.blog.models import Post
from deejango.drinker.models import Drinker
from forms import CommentForm

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
	post = get_object_or_404(Post, slug=postslug)
	form = CommentForm(request.POST or None)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.post = post
		comment.author = Drinker.objects.get(user=request.user)
		comment.save()
		return redirect(request.path)

	context = {'post': post, 'form': form}
	return render_to_response('specific_post.html', context, RequestContext(request))