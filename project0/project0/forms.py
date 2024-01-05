from django import forms
from .models import UserProfile, Item, Inquiry

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name','phone', 'email','university', 'student_id',)  # Add more fields as needed for the user profile

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'description', 'category', 'price')  # Add more fields for item details

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ('title', 'description',)  # Add more fields for inquiry details
