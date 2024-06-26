from django.shortcuts import render
from django.http import JsonResponse
from base.models import ListKhodam, ResponseLog
import random
from django.utils import timezone

def home(request):
    return render(request, 'base/cek-khodam.html')

def cek_khodam(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        
        khodams = list(ListKhodam.objects.values_list('nama_khodam', flat=True))
        
        if khodams:
            khodam = random.choice(khodams)
            current_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            response_data = {
                'code': 200,
                'status': 'Success',
                'message': 'Successfully retrieved khodam data',
                'data': {
                    'name': name,
                    'khodam': khodam
                },
                'current_time': current_time
            }
            # Save to database
            log_entry = ResponseLog(
                code=response_data['code'],
                status=response_data['status'],
                message=response_data['message'],
                name=response_data['data']['name'],
                khodam=response_data['data']['khodam'],
                current_time=response_data['current_time']
            )
            log_entry.save()

            return JsonResponse(response_data)
        else:
            response_data = {
                'code': 404,
                'status': 'Error',
                'message': 'No khodam data available',
                'data': {
                    'name': None,
                    'khodam': None
                },
                'current_time': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            # Save to database
            log_entry = ResponseLog(
                code=response_data['code'],
                status=response_data['status'],
                message=response_data['message'],
                name=response_data['data']['name'],
                khodam=response_data['data']['khodam'],
                current_time=response_data['current_time']
            )
            log_entry.save()

            return JsonResponse(response_data, status=404)
    
    response_data = {
        'code': 400,
        'status': 'Error',
        'message': 'Invalid request',
        'data': {
            'name': None,
            'khodam': None
        },
        'current_time': timezone.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    # Save to database
    log_entry = ResponseLog(
        code=response_data['code'],
        status=response_data['status'],
        message=response_data['message'],
        name=response_data['data']['name'],
        khodam=response_data['data']['khodam'],
        current_time=response_data['current_time']
    )
    log_entry.save()

    return JsonResponse(response_data, status=400)
