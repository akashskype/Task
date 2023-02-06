from django.urls import path
from .views import login_view, register_view, show_users, logout_view, add_department, show_departments, assign_department, user_homepage, admin_homepage, delete_department
urlpatterns = [
    path('', login_view, name='home'),
    path('register/', register_view, name='register'),
    path('show/', show_users, name='show-users'),
    path('logout/', logout_view, name='logout'),
    path('department/', add_department, name='add-department'),
    path('show_department/', show_departments, name='show-departments'),
    path('assign_department/<int:pk>/', assign_department, name='assign-department'),
    path('userhome/', user_homepage, name='user'),
    path('adminhome/', admin_homepage, name='admin'),
    path('dv/<int:pk>', delete_department, name='delete'),
    
]