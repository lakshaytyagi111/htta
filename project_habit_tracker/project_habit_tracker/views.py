from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Habit
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserProfileForm, HabitForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import HabitClick
from .forms import HabitForm
from .models import Habit
import datetime
from datetime import timedelta
import json


@login_required
def all_functions(request):
    form = HabitForm()

    if request.method == 'POST':
        if 'habit_id' in request.POST:  # Remove habit if submitted
            habit_id = request.POST['habit_id']
            habit = Habit.objects.get(id=habit_id, user=request.user)
            habit.delete()
            return JsonResponse({'message': 'Habit removed successfully'})

        form = HabitForm(request.POST)
        if form.is_valid():  # Add habit if submitted
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return JsonResponse({'message': 'Habit added successfully'})
    
    #return HttpResponse(json.dumps(event_arr))
    
    habits = Habit.objects.filter(user=request.user)
    habit_clicks = HabitClick.objects.filter(habit__in=habits).order_by('clicked_date')
    # habit_clicks2 = HabitClick.objects.filter(user=request.user)
    context = {'form': form, 'habits': habits, 'habit_clicks': habit_clicks}
    return render(request, 'all_functions.html', context)

def save_habit_click(request):
    
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        habit_id = request.POST.get('habit_id')
        clicked_date_str = request.POST.get('clicked_date')

        # Convert the string date to a datetime object
        clicked_date = datetime.datetime.strptime(clicked_date_str, '%Y-%m-%d').date()

        # Check if a habit click entry exists for the clicked date
        habit_click_exists = HabitClick.objects.filter(
            habit_id=habit_id,
            clicked_date=clicked_date,
            habit__user=request.user
        ).exists()

        if habit_click_exists:
            # If entry exists, delete it
            HabitClick.objects.filter(
                habit_id=habit_id,
                clicked_date=clicked_date,
                habit__user=request.user
            ).delete()
            return JsonResponse({'message': 'Habit click removed'})
        else:
            # If entry doesn't exist, create a new one
            HabitClick.objects.create(
                habit_id=habit_id,
                clicked_date=clicked_date,
            )
            return JsonResponse({'message': 'Habit click saved'})
    return JsonResponse({}, status=400)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/allfunctions/')  # Redirect to dashboard or any desired page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# @login_required
# def profile(request):
#     user = request.user

#     if request.method == 'GET':
#         form = UserProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Redirect to profile page after saving profile info
#             return redirect('profile')
        
#     else:
#         return render(request, 'profile.html')

        
#     return render(request, 'profile.html', {'form': form})
