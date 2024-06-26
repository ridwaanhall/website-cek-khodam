from django.shortcuts import render
from django.http import JsonResponse
import random

def home(request):
    return render(request, 'base/cek-khodam.html')

def input(request):
    if request.method == 'POST':
        name = request.POST.get('name-username', '')
        responses = ["batu kodok", "lalat", "pintu"]
        response = random.choice(responses)
        return JsonResponse({'name': name, 'response': response})
    return JsonResponse({'response': 'Invalid request'}, status=400)
