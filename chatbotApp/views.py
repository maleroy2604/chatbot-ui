from django.shortcuts import render
from .forms import MessageForm
from django.http import JsonResponse
import requests

def home(request): 
    form = MessageForm()
    return render(request, 'home.html', {'form': form})

def getMessages(request):
    txt = request.GET['text']
    response = requests.get('http://localhost:5000/getMessages/{}'.format(txt))
    return JsonResponse(response.json())

    
