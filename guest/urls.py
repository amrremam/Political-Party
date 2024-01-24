from django.urls import path
from .views import guest_all

app_name = 'guest'

urlpatterns = [
    path('', guest_all, name='guest')
]
