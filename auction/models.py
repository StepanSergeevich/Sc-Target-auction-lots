from django.contrib.auth.models import User
from django.db import models


#Модель выбора лотов пользователем
class ClientSelection(models.Model):
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_items = models.JSONField(default=list)

    def __str__(self):
        return f"Selection for client_id {self.client_id.username}"
