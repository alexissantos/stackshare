import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.conf import settings

import requests

root_url = "https://api.stackshare.io/"
access_token_string = "&access_token=" + settings.STACKSHARE_API_KEY

def start(request):

    template = "start.html"

    # Get 50 random tools from Stackshare
    stackshare = requests.get(root_url + "v1/tools/explore?layer_id=1" + access_token_string)

    # Print the names of the first three tools Stackshare returns
    print stackshare.json()[1]['name']
    print stackshare.json()[2]['name']
    print stackshare.json()[3]['name']

    return render_to_response(template, dict({
    }), context_instance=RequestContext(request))