from django.urls import path
from .views import AddUser


urlpatterns = [
    path('add_user/', AddUser.as_view(), name='add_user'),
    # path('edit/<int:user_id>/', edit_user, name='edit_user'),
    # path('delete/<int:user_id>/', delete_user, name='delete_user'),
]
