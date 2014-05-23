from django.shortcuts import render
from rc.models import Coordinator, RemoteCenter
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
def index(request):
	context=RequestContext(request)#RequestContext must be an constructor
	coords=Coordinator.objects.all()
	rc=RemoteCenter.objects.all()
	context_dict={'coords':coords,'rc':rc}
	return render_to_response('show_rc_details.html',context_dict,context)
