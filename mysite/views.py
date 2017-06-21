from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime


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