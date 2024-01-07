from django.urls import path
from .views import edit_user, delete_user



urlpatterns = [
    path('edit/<int:user_id>/', edit_user, name='edit_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
]
