from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import request
from django.views.generic import TemplateView
from django.conf import settings
from .models import HUMIDITY, TEMP

# Create your views here.

class IndexView(TemplateView):

    template_name = 'BDB_monitoring/index.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)

class LoginView(TemplateView):

    template_name = 'BDB_monitoring/login.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)

class MonitoringView(TemplateView):

    template_name = 'BDB_monitoring/monitoring.html'

    def get(self, request, **kwargs):
        context = {
            'humidity':str(HUMIDITY),
            'temp':str(TEMP),
        }
        return render(request, self.template_name, context)
