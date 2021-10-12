from django.urls import path, include
from .views import TodoCreate, TodoList, TodoDetail, TodoDelete, TodoUpdate

urlpatterns = [
    path('list/', TodoList.as_view(), name = 'list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name = 'detail'),
    path('create', TodoCreate.as_view(), name = 'create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name = 'delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name = 'update'),
]
