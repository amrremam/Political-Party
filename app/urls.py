from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('app/', views.index, name='dashboard'),

    path('newUser/', views.new_user, name='newUser'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('roles/', views.roles, name='roles'),

    path('table/', views.table, name='table'),

    path('tables/', views.tables, name='tables'),

    path('permission/', views.permission, name='permission'),

    path('addDor/', views.addDor, name='addDor'),
]
