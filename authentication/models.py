from django.db import models

#Модель временного пользователя для проверки валидности кода 
class PendingUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    confirmation_code = models.CharField(max_length=100)
    password = models.CharField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.username} - {self.confirmation_code}'

