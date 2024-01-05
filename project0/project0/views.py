from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Item
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserProfileForm, ItemForm
from django.http import HttpResponseRedirect

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/dashboard/')  # Redirect to dashboard or any desired page
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

@login_required
def profile(request):
    user = request.user

    if request.method == 'GET':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to profile page after saving profile info
            return redirect('profile')
        
    else:
        return render(request, 'profile.html')

        
    return render(request, 'profile.html', {'form': form})

@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('item_detail', item_id=item.id)  # Redirect to item detail page
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})

def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'item_detail.html', {'item': item})

def all_items(request):
    items = Item.objects.all().order_by('-created_at')
    return render(request, 'all_items.html', {'items': items})

@login_required
def edit_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.user == item.user:  # Allowing only the item owner to edit
        if request.method == 'POST':
            form = ItemForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('item_detail', item_id=item.id)  # Redirect to item detail page after edit
        else:
            form = ItemForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})
    else:
        # Handle unauthorized access or redirect to an error page
        return redirect('item_detail', item_id=item.id)  # Redirect to item detail page

@login_required
def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    if request.user == item.user:  # Allowing only the item owner to delete
        if request.method == 'POST':
            item.delete()
            return redirect('all_items')  # Redirect to all items page after deletion
        return render(request, 'delete_item.html', {'item': item})
    else:
        # Handle unauthorized access or redirect to an error page
        return redirect('item_detail', item_id=item.id)  # Redirect to item detail page

@login_required
def user_items(request):
    user_items = Item.objects.filter(user=request.user)
    return render(request, 'user_items.html', {'user_items': user_items})

# def search_items(request):
#     query = request.GET.get('q')
#     items = Item.objects.filter(title__icontains=query) if query else Item.objects.all()
#     return render(request, 'search_items.html', {'items': items, 'query': query})

# def category_items(request, category):
#     items = Item.objects.filter(category=category)
#     return render(request, 'category_items.html', {'items': items, 'category': category})
