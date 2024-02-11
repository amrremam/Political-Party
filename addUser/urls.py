from django.urls import path
from .views import AddUser, show_user, delete_user, update_user, user_profile


app_name = 'addUser'


urlpatterns = [
    path('add_user/', AddUser.as_view(), name='add_user'),
    path('show_user/', show_user, name='show_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('user_profile/<int:user_id>/', user_profile, name='user_profile')
]
