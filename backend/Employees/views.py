from django.http import HttpResponse, Http404
from django.template import Context, loader
from Employees.models import Employee, EmployeeForm
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.forms.models import modelformset_factory

def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def index(request):
    all_employees = Employee.objects.all()
    t = loader.get_template('view_employees.html')
    c = RequestContext(request, {
        'all_employees': all_employees,
	}, [ip_address_processor])
    return HttpResponse(t.render(c))
def individual_employee(request, idnum):
	try:
		id_num = int(idnum)
	except ValueError:
		raise Http404()
	html = "<html><body>Id number is %s.</body></html>" % (id_num)
	return HttpResponse(html)
