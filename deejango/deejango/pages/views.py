from django.shortcuts import render_to_response
from django.template import RequestContext
from deejango.pages.models import HomePage

def home_page(request):
	homepage = HomePage.objects.get(pk=1)
	context = {'homepage': homepage}
	return render_to_response('test_area_two.html',
								context,
								context_instance=RequestContext(request))
