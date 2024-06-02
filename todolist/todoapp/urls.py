from django.urls import path
from .views import index, add, delete, update
app_name = 'todoapp'

urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete')
]