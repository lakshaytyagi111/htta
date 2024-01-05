from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    # Add additional fields related to the user profile (e.g., university, student ID, etc.)
    # Example:
    # university = models.CharField(max_length=100)
    # student_id = models.CharField(max_length=20)
    # ...

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add other fields related to the item (e.g., category, price, images, etc.)
    # Example:
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    # ...

class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add other fields related to the inquiry if needed
    # ...

class UserMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
