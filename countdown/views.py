from django.http import *
from django.template import RequestContext, loader
from datetime import date

import os
import sys
import Image
import MySQLdb


def countdown(request):
  now = date.today()
  event_date = date(2014, 7, 31)
  days = str(event_date - now)[:-9]
  t = loader.get_template('margie.html')
  c = RequestContext(request, {'days': days,})
  return HttpResponse(t.render(c))

  
