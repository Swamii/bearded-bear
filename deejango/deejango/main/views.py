from django.shortcuts import redirect, render, render_to_response
from django.core.mail import mail_admins
from django.template import RequestContext
from deejango.main.forms import ContactForm

def index(request):
    return render_to_response('index.html',
                              locals(),
                              context_instance=RequestContext(request))

def test_area(request):
    return render_to_response('hero.html',
                              locals(),
                              context_instance=RequestContext(request))

'''
def contact_form(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "From: %s <%s>\r\nSubject:%s\r\nMessage:\r\n%s\r\n" % (
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['subject'],
                form.cleaned_data['message']
            )
            mail_admins('Contact form', message, fail_silently=False)
            if request.is_ajax():
                return render(request, 'success.html')
            else:
                return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'form.html', {'form': form})
'''