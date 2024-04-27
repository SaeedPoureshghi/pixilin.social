import json
from django.http import JsonResponse


class CaptchaMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        if request.path == '/api/v1/login':
            if request.method == 'POST':
                print(request.body)
                pass
            else:
                    return JsonResponse({'error': 'Invalid Captcha!'}, status=400)
            
        
        response = self.get_response(request)
        return response