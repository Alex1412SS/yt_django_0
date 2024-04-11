from django.urls import path
from bluepage import views
app_name= "myapp"
urlpatterns = [
    path('', views.Ai_tools_ai.as_view(), name='baze'),
    path('<int:pk>/', views.Ai_tools_detail.as_view(), name='detail'),
    path('additem/', views.add_ai, name='add'),
    path('updateitem/<int:id_my>/', views.updateitem, name='updateitem'),
    path('deleteitem/<int:id_my>', views.deleteitem, name='deleteitem')
]
