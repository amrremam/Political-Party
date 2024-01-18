from django.urls import path
from .views import login_view, index, roles, tables

app_name = 'app'


urlpatterns = [
    path('', index, name='dashboard'),

    path('login/', login_view, name='login'),

    path('roles/', roles, name='roles'),

    path('tables/', tables, name='tables'),
]
