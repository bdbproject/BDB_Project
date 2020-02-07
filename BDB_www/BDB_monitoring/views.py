from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import request, HttpResponse
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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
    
    def post(self, request, **kwargs):
        postData = request.POST.copy()
        username = postData.get('username', None)
        password = postData.get('password', None)
        response = None

        if request.user.is_authenticated:
            response = HttpResponse('already logged')
            return response

        if username == None or password == None:
            response = HttpResponse('username and password must be specified')
            return response

        user = authenticate(username=username, password=password)

        if user == None or user.is_active == False:
            response = HttpResponse('invalid')
            return response
        
        login(request, user)
        
        response = HttpResponse('ok')
        return 

class MonitoringView(TemplateView):

    template_name = 'BDB_monitoring/monitoring.html'

    def get(self, request, **kwargs):
        context = {
            'humidity':str(HUMIDITY),
            'temp':str(TEMP),
        }
        return render(request, self.template_name, context)
