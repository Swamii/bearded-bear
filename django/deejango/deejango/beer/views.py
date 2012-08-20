from django.shortcuts import render_to_response
from django.template import RequestContext
from deejango.beer.models import Beer, Brewery


def beers_all(request):
	beers = Beer.objects.all().order_by('name')
	breweries = Brewery.objects.all().order_by('name')
	context = {'beers': beers, 'breweries': breweries}
	return render_to_response('beer.html',
								context,
								context_instance=RequestContext(request))

def specific_beer(request, beerslug):
	beer = Beer.objects.get(slug = beerslug)
	context = {'beer': beer}
	return render_to_response('single_beer.html',
								context,
								context_instance=RequestContext(request))

def specific_brewery(request, breweryslug):
	brewery = Brewery.objects.get(slug=breweryslug)
	beers = Beer.objects.filter(brewery=brewery)
	context = {'beers': beers}
	return render_to_response('single_brewery.html',
								context,
								context_instance=RequestContext(request))