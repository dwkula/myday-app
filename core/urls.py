from django.urls import path
from .views import TaskPage, TaskAdd, TaskEdit, TaskRemove, UserLogin, UserRegistration
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', UserRegistration.as_view(), name='register'),
    path('', TaskPage.as_view(), name='tasks'),
    path('task-create/', TaskAdd.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskEdit.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskRemove.as_view(), name='task-delete'),

]


