from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField()


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_name = models.CharField(max_length=101)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.habit_name
    
class HabitClick(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    clicked_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default= '0')
 