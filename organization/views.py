# Create your views here.
from django.http import HttpResponse
from organization.models import *

try:
	import json
except:
	import simplejson as json

def view_year(request, year):
	y = Year.objects.get(name = year)
	res = [{
		"section":str(s),
		'url':str(s.url()),
		'description':s.description
	} for s in y.sections.all()]
	return HttpResponse(json.dumps(res))

def view_section(request, year, section):
	y = Year.objects.get(name = year)
	s = SchoolSection.objects.get(year = y, suffix = section)
	res = [{
		"course":str(c),
		'url':str(c.url()),
		'description':c.description
	} for c in s.courses.all()]
	return HttpResponse(json.dumps(res))



def view_course(request, year, section, course):
	y = Year.objects.get(name = year)
	s = SchoolSection.objects.get(year = y, suffix = section)
	c = Course.objects.get(section = s, name = course)
	res = [{
		"klass":str(k),
		'url':str(k.url()),
		'students':k.students.all().count(),
		'teachers':k.teachers.all().count(),
	} for k in c.klasses.all()]
	return HttpResponse(json.dumps(res))

	
	
	

def view_klass(request, year,section, course, klass):
	y = Year.objects.get(name = year)
	s = SchoolSection.objects.get(year = y, suffix = section)
	c = Course.objects.get(section = s, name = course)
	k = Klass.objects.get(course = c, name = klass)
	res = []
	for q in k.students.all():
		res.append({
			'type':"student",
			"name":str(q),
			#'url':str(q.url()),
			} )
	for q in k.teachers.all():
		res.append({
			'type':"teacher",
			"name":str(q),
			#'url':str(q.url()),
			} )

	return HttpResponse(json.dumps(res))