from django.urls import path
from .views import index, roles, tables, signin

app_name = 'app'

urlpatterns = [
    path('', index, name='dashboard'),
    path('roles', roles, name='roles'),
    path('tables', tables, name='tables'),
    path('signin/', signin, name='sign-in'),
]
