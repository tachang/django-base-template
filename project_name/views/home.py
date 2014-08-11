from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def index(request):

    c = {
    }

    return render_to_response('home.html', c, context_instance=RequestContext(request))
