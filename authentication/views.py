from .utils import send_confirmation_email, generate_confirmation_code
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from auction.models import ClientSelection
from django.shortcuts import render
from django.contrib import messages
from .models import PendingUser


# Регистрация и Авторизация
def authentication(request):

    form = RegisterForm()
    login_form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if 'login' in request.POST:  
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/auction/main')
                else:
                    messages.error(request, 'Неправильный пароль или имя пользователя.', extra_tags='sign_in')
                    return redirect('authentication')

        elif 'register' in request.POST:  
            form = RegisterForm(request.POST)

            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']  
                
                pennding_user = PendingUser.objects.filter(username=username).first()
                if pennding_user:
                    pennding_user.delete()

                confirmation_code = generate_confirmation_code()
                PendingUser.objects.create(username=username, email=email, confirmation_code=confirmation_code, password = password)
                send_confirmation_email(email, confirmation_code)
                return render(request, 'authentication/confirmation_sent.html')
            
            else:
                messages.error(request, 'Ошибки регистрации:', extra_tags='wrong_register')
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{error}", extra_tags='wrong_register')
    
    return render(request, 'authentication/authentication.html', {'form': form, 'login_form': login_form})


# Верификация email 
def verifity_email(request):
    if request.method == 'POST':
        if 'verify_code' in request.POST:  
            code = request.POST.get('code')

            try:
                pending_user = PendingUser.objects.get(confirmation_code=code)


                user = User.objects.create_user(
                    username=pending_user.username,
                    email=pending_user.email,
                    password=pending_user.password  
                )
                ClientSelection.objects.create(client_id=user, selected_items=["y40kk", "olz36", "55621", "z301y", "gn975", "4q7pl"])

                pending_user.delete()

                return redirect('http://127.0.0.1:8000/auction/main')

            except PendingUser.DoesNotExist:
                messages.error(request, "Неверный код подтверждения. \n Пожалуйста, попробуйте снова.", extra_tags='verifity_error')

    return render(request, 'authentication/confirmation_sent.html')

