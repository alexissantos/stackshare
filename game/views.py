import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.conf import settings

import requests

root_url = "https://api.stackshare.io/"

def start(request):

    template = "start.html"

    print settings.STACKSHARE_API_KEY

    return render_to_response(template, dict({
    }), context_instance=RequestContext(request))