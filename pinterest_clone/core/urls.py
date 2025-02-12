# core/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView  # Import the LogoutView
from .views import home, register, create_board, board_detail, create_pin, add_pin, delete_board, profile, CustomLoginView

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('create_board/', create_board, name='create_board'),
    path('board/<int:board_id>/', board_detail, name='board_detail'),
    path('board/<int:board_id>/create_pin/', create_pin, name='create_pin'),
    path('board/<int:board_id>/add_pin/', add_pin, name='add_pin'),
    path('board/<int:board_id>/delete/', delete_board, name='delete_board'),
    path('profile/', profile, name='profile'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Ensure this line is present
]