from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings
from Adafruit_DHT import *

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
        humidity, temp = read_retry(DHT11, 23, 3, 5)
        context = {
            'humidity':str(humidity),
            'temp':str(temp),
        }
        return render(request, self.template_name, context)
