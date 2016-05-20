import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string
from django.conf import settings

import requests
import random

root_url = "https://api.stackshare.io/"
api_key = settings.STACKSHARE_API_KEY

def start(request):

    # Template used for rendering the page
    template = "start.html"

    # Create list to hold tools that have reasons
    tools = []
    # Continue adding tools to the list until there are a total of 4.
    # The while loop may seem excessive, but after some testing, it
    # seemed like there were a few occasions where there weren't 4
    # tools with 3 or more reasons in the 50 tools the Stackshare API provided.
    while len(tools) < 3:
        # Get 50 random tools from Stackshare
        stackshare = requests.get(root_url + "v1/tools/explore?layer_id=1&access_token=" + api_key)
        # Loop through tools returned by the Stackshare API
        for tool in stackshare.json():
            # If a tool has three or more easons, append it to the list
            if len(tool['reasons']) >= 3:
                tools.append(tool)
    # Pick a random number to make one tool the correct choice
    correct_tool = random.randint(0,3)

    return render_to_response(template, dict({
        "tool_one": tools[0],
        "tool_two": tools[1],
        "tool_three": tools[2],
        "tool_four": tools[3],
        "correct_tool": tools[correct_tool],
    }))

def choose_tool(request, chosen_id, correct_id):

    # Template used to update the start page
    template = "chosen.html"

    # Check if players chose the right tool
    if chosen_id == correct_id:
        # Boolean to check in template if player is correct
        player_is_correct = True
        # Request info on CHOSEN tool from Stackshare
        chosen = requests.get(root_url + "v1/tools/" + chosen_id + "?&access_token=" + api_key)
        # Make the correct tool the same as the chosen tool
        correct = chosen
    else:
        # Boolean to check in template if player is correct
        player_is_correct = False
        # Request info on CHOSEN tool from Stackshare
        chosen = requests.get(root_url + "v1/tools/" + chosen_id + "?&access_token=" + api_key)
        # Request info on CORRECT tool from Stackshare
        correct = requests.get(root_url + "v1/tools/" + correct_id + "?&access_token=" + api_key)

    response = {
        "status": "OK",
        "html": render_to_string(
            "chosen.html",
            RequestContext(request, {
                "chosen": chosen.json(),
                "correct": correct.json(),
                "player_is_correct": player_is_correct,
            })
        )
    }
    return HttpResponse(json.dumps(response), content_type="application/json")