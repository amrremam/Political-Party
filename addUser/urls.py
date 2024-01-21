from django.urls import path
from .views import AddUser, UserList


urlpatterns = [
    path('add_user/', AddUser.as_view(), name='add_user'),
    path('user_list/', UserList.as_view(), name='user_list'),
    # path('delete/<int:user_id>/', delete_user, name='delete_user'),
]
