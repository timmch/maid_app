from django.http import HttpResponse, Http404
from django.template import Context, loader
from Employees.models import Employee, EmployeeForm
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User, Group
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def index(request):
    all_employees = User.objects.all()
	#filter(groups__name='Manager') to filter by group name
    t = loader.get_template('view_employees.html')
    c = RequestContext(request, {
        'all_employees': all_employees,
	}, [ip_address_processor])
    return HttpResponse(t.render(c))


