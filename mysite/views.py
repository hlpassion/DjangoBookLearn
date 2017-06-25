from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.form import ContactForm
from django.core.mail import send_mail, get_connection


def hello(request):
    return HttpResponse('Hello World, Hello Django')


def bye(request):
    return HttpResponse('Bye Django! Sleeping!!!')


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date':now})
    # t = get_template('current_datetime.html')
    # html = t.render({'current_date':now})
    # return HttpResponse(html)


def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	# html = "<html><body>In %d hour(s), it will be %s</body></html>"  % (offset, dt)
	# return HttpResponse(html)
	return render(request, 'hours_ahead.html', {'hour_offset':offset, 'next_time':dt})


def ua_display(request):
    values = request.META.items()
    print(values) 
    html = []
    for k in sorted(values):
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, k[-1]))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                connection=con
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!'}
        )

    return render(request, 'contact_form.html', {'form': form})


def contact_thanks(request):
    return HttpResponse('Thanks for contact us!!')