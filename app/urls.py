from django.urls import path
from .views import login_view, logout_view, index, roles, tables, permission, addDor, table, new_user

app_name = 'app'


urlpatterns = [

    path('app/', index, name='dashboard'),

    path('newUser/', new_user, name='newUser'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),

    path('roles/', roles, name='roles'),

    path('table/', table, name='table'),

    path('tables/', tables, name='tables'),

    path('permission/', permission, name='permission'),

    path('addDor/', addDor, name='addDor'),

]
