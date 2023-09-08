from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class ToDoItem(models.Model):
    title = models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reminder(models.Model):
    todo_item = models.ForeignKey(ToDoItem, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return f"Reminder for {self.todo_item.title}"

