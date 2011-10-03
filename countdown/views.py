from django.http import HttpResponse
from django.template import RequestContext, loader
from datetime import date
from django.core.mail import send_mail


def countdown(request):
  now = date.today()
  event_date = date(2014, 7, 31)
  days = str(event_date - now)[:-9]
  if (days % 1032) == 0:
      rec = ['kim.a.pettersen@gmail.com']
      send_mail(
              'emailsubject', 
              'This is a email sent from django',
              'kim.a.pettersen@gmail.com',
              rec,
              )
  t = loader.get_template('margie.html')
  c = RequestContext(request, {'days': days,})
  return HttpResponse(t.render(c))

  
