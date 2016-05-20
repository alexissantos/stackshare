from django.conf.urls import url
import game.views

urlpatterns = [
    url(r"^$", game.views.start, name="start"),
    url(r"^choose/(?P<chosen_id>\d+)/(?P<correct_id>\d+)/$", game.views.choose_tool, name="choose_tool"),
]