from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse('Hello World, Hello Django')


def bye(requesr):
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


