from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('roles', views.roles, name='roles'),
    path('tables', views.tables, name='tables'),
    path('signin/', views.signin, name='sign-in'),
]
