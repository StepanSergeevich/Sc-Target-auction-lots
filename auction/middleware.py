from django.shortcuts import redirect


# Функция проверки авторизации пользователя
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        print(request.path)
        if not request.user.is_authenticated and request.path in ['/auction/main/', '/auction/profile_user/']:
            return redirect('http://127.0.0.1:8000/auth/authentication')
        if request.user.is_authenticated and request.path in ['/auth/authentication', '/auth/confirmation']:
            return redirect('http://127.0.0.1:8000/auction/main')
        return self.get_response(request)