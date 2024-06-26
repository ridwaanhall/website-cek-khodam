from django.shortcuts import render
from django.http import JsonResponse
from base.models import ListKhodam
import random
from datetime import datetime

def home(request):
    return render(request, 'base/cek-khodam.html')

def input(request):
    if request.method == 'POST':
        name = request.POST.get('name-username', '')
        
        khodams = list(ListKhodam.objects.values_list('nama_khodam', flat=True))
        
        if khodams:
            response = random.choice(khodams)
            current_time = datetime.now().strftime('%Y%m%d%H%M%S')
            return JsonResponse({'name': name, 'response': response, 'datetime_now': current_time})
        else:
            return JsonResponse({'response': 'No khodam data available'}, status=404)
    
    return JsonResponse({'response': 'Invalid request'}, status=400)
