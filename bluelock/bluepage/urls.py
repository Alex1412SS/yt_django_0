from django.urls import path
from bluepage import views
app_name= "myapp"
urlpatterns = [
    path('', views.nigga),
    path('<int:id_my>/', views.index, name='detail'),
]
