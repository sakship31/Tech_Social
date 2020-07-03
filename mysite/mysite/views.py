from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class index(TemplateView):
    template_name = "index.html"


class loggedin(TemplateView):
    template_name = 'loggedin.html'

class loggedout(TemplateView):
    template_name = 'loggedout.html'

