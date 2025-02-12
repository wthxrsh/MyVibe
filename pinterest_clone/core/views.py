# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .models import Board, Pin

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# Home view to display all pins
def home(request):
    pins = Pin.objects.all()  # Fetch all pins from the database
    return render(request, 'core/home.html', {'pins': pins})

# View to create a new board
# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Board

@login_required
def create_board(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # Get the board name from the form
        if name:  # Check if the name is provided
            board = Board.objects.create(name=name, user=request.user)
            return redirect('board_detail', board_id=board.id)  # Redirect to the new board's detail page
        else:
            # Handle the case where the name is not provided (optional)
            return render(request, 'core/create_board.html', {'error': 'Board name is required.'})
    return render(request, 'core/create_board.html')

# core/views.py
# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pin, Board

# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pin, Board

@login_required
def add_pin(request, board_id):
    board = get_object_or_404(Board, id=board_id)  # Get the board or return 404 if not found
    if request.method == 'POST':
        image = request.FILES.get('image')  # Get the uploaded image
        title = request.POST.get('title')  # Get the title
        if image and title:
            Pin.objects.create(image=image, title=title, board=board, user=request.user)  # Create the pin
            return redirect('board_detail', board_id=board.id)  # Redirect to the board detail page
        else:
            return render(request, 'core/add_pin.html', {'board': board, 'error': 'All fields are required.'})
    return render(request, 'core/add_pin.html', {'board': board})
# View to display details of a specific board
@login_required
def board_detail(request, board_id):
    board = get_object_or_404(Board, id=board_id)  # Get the board or return 404 if not found
    pins = board.pins.all()  # Get all pins associated with the board
    return render(request, 'core/board_detail.html', {'board': board, 'pins': pins})

# View to create a new pin associated with a specific board
@login_required
def create_pin(request, board_id):
    board = get_object_or_404(Board, id=board_id)  # Get the board or return 404 if not found
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        Pin.objects.create(title=title, image=image, board=board)  # Create a new pin
        return redirect('board_detail', board_id=board.id)  # Redirect to the board's detail page
    return render(request, 'core/create_pin.html', {'board_id': board_id})

# Login view using Django's built-in authentication views
class CustomLoginView(auth_views.LoginView):
    template_name = 'core/registration/login.html'  # Specify the custom login template

# core/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user  # Get the currently logged-in user
    return render(request, 'core/profile.html', {'user': user})  # Pass the user to the template
# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Board

@login_required
def delete_board(request, board_id):
    board = get_object_or_404(Board, id=board_id, user=request.user)  # Ensure the user owns the board
    board.delete()  # Delete the board
    return redirect('profile')  # Redirect to the profile page after deletion

# core/views.py
