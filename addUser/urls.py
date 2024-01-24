from django.urls import path
from .views import AddUser, show_user


urlpatterns = [
    path('add_user/', AddUser.as_view(), name='add_user'),
    path('show_user/', show_user, name='show_user'),
    # path('delete/<int:user_id>/', delete_user, name='delete_user'),
]
