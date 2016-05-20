from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("game.views",
    url(r"^$", "start", name="start"),
    url(r"^choose/(?P<chosen>\d+)/(?P<winner>\d+)/$", "choose_tool", name="choose_tool"),
)