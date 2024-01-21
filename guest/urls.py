from django.urls import path
from .views import guest_list

app_name = 'guest'

urlpatterns = [
    path('', guest_list, name='guest')
]
