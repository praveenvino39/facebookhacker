from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Credential
# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        newlogin = Credential(username = username, password = password)
        newlogin.save()

    return render(request, 'homepage/index.html')
