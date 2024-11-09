
from .models import ClientSelection
from django.contrib import admin

class ClientSelectionAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'selected_items')  
    search_fields = ('client_id__username',)  

admin.site.register(ClientSelection, ClientSelectionAdmin)