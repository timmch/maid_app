from django.http import HttpResponse
from Employees.models import Employee, EmployeeForm
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.forms.models import modelformset_factory

def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def index(request):
    all_employees = Employee.objects.all()
    t = loader.get_template('employees/view_employees.html')
    c = RequestContext(request, {
        'all_employees': all_employees,
	}, [ip_address_processor])
    return HttpResponse(t.render(c))
