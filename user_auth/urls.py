from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.createuser,name='createuser') ,
    path('login',views.loginuser,name='loginuser'),
    path('signout',views.signout,name='signout'),
    path('createtodo',views.createusertodo,name='createusertodo'),
    path('showtodos/<int:todo_pk>',views.showtodos,name='showtodos'),
    path('del/<int:pk>',views.delete_todo,name='deletetodo'),
]