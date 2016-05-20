import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.conf import settings

import requests
import random

root_url = "https://api.stackshare.io/"
access_token_string = "&access_token=" + settings.STACKSHARE_API_KEY

def start(request):

    template = "start.html"

    # Get 50 random tools from Stackshare
    stackshare = requests.get(root_url + "v1/tools/explore?layer_id=1" + access_token_string)

    # The following print lines are for debugging in the console
    # Print the names of the first tool Stackshare returns
    print stackshare.json()[0]['name']

    # Print the resons people like it
    for reason in stackshare.json()[0]['reasons']:
        print reason['one_liner']

    # Print a space
    print '\n'

    # Pick a random number to make one tool the correct choice
    correct_tool = random.randint(1,4)

    return render_to_response(template, dict({
        "tool_one": stackshare.json()[0],
        "tool_two": stackshare.json()[1],
        "tool_three": stackshare.json()[2],
        "tool_four": stackshare.json()[3],
    }), context_instance=RequestContext(request))