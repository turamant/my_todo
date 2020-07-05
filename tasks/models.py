from django.db import models

# Create your models here.
from users.models import CustomUser


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False, verbose_name='Завершеность(поставьте галочку, если исполнено) ')
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=True, related_name='users')
    def __str__(self):
        return self.title