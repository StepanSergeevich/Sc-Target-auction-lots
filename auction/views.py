from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
from channels.db import database_sync_to_async
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import ClientSelection
from django.contrib import messages
from django.shortcuts import render
from .scripts.Api import ApiClient
from .utils import LIST_ITEMS
import asyncio


# Выход с аккаунта 
def logout_view(request):
    logout(request)  
    return redirect('main')   


# Настройки профиля
def profile_user(request):
    username = request.user.username
    email = request.user.email
    context = {'username': username, 'email': email}
    return render(request, 'auction/profile_user.html', context)

# Настройки вывода Лотов
def choice_lots(request):

    if request.method == 'POST':
        if 'choiced' in request.POST:
            selected_items = request.POST.getlist('selected_items')
            ClientSelection.objects.update_or_create(client_id = request.user, defaults={'selected_items': selected_items})
            messages.success(request, 'Список лотов изменён!')
            return render(request, 'auction/profile_user.html')
        
    checkbox_values = LIST_ITEMS
    client_selection = ClientSelection.objects.filter(client_id=request.user).first()
    selected_items = client_selection.selected_items if client_selection else []
    return render(request, 'auction/choice_lots.html', {'selected_items': selected_items, 'checkbox_values': checkbox_values,})



# Смена пароля
class change_password(PasswordChangeView):
    template_name = 'auction/change_password.html'
    success_url = reverse_lazy('profile_user')

    def form_valid(self, form):
        user = form.save()
        update_session_auth_hash(self.request, user)
        messages.success(self.request, 'Пароль изменён!')  
        return super().form_valid(form)
        

    def form_invalid(self, form):
        if self.request.method == 'POST':
            if 'change' in self.request.POST:
                user = self.request.user 
                old_password = form.cleaned_data.get('old_password')

                if not user.check_password(old_password):
                    form.add_error('new_password2', 'Старый пароль неверен.')

                return super().form_invalid(form)
            
        return super().form_invalid(form)
            


# Подключение к БД
@database_sync_to_async
def connect_data_base(request):
    selection = ClientSelection.objects.get(client_id=request.user)
    return selection.selected_items


# Обновление лотов на главной странице(Вывод страницы main)
async def user_lots(request):
    item_ids = await connect_data_base(request)

    async def fetch_lots_price(item_id):
        client = ApiClient(item_id)
        price_info = await client.get_item_price()
        return {**price_info, 'item_id': LIST_ITEMS[item_id], 'img_src':f"../../static/auction/images/{item_id}.png"}

    tasks = [fetch_lots_price(item_id) for item_id in item_ids]
    info_items_lots = await asyncio.gather(*tasks)
    print(info_items_lots)
    context = {'API':info_items_lots}
    return render(request, 'auction/main.html', context = context)


def main(request):
    return render(request, 'auction/main.html')