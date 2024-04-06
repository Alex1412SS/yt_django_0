from django.urls import path
from users import views
from django.contrib.auth.views import LoginView
app_name = "user_app"
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<str:username>', views.profile, name='profile'),
]
