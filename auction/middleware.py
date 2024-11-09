from django.shortcuts import redirect
from django.shortcuts import render

# Функция проверки авторизации пользователя
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path in ['/auction/main/', '/auction/profile_user/']:
            return redirect('http://127.0.0.1:8000/auth/authentication/')
        
        if request.user.is_authenticated and request.path in ['/auth/authentication/', '/auth/confirmation/']:
            return redirect('http://127.0.0.1:8000/auction/main/')
        
        return self.get_response(request)

class ErrorLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Проверяем, является ли ответ редиректом
        if response.status_code >= 400 and not response.has_header('Location'):
            if response.status_code == 404:
                return render(request, 'auction/404.html', status=404)
            elif response.status_code == 500:
                return render(request, 'auction/500.html', status=500)

        return response