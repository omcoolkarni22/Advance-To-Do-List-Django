from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='hello'),
    path('login', views.Login, name='login'),
    path('register', views.Register, name='register'),
    path("logout", views.Logout, name='logout'),
    path('archive_task', views.Archive, name='show_archive'),
    path('add_tasks', views.add_tasks, name='add_task'),
    path('changes_in_task/<int:id>', views.Update, name='update_tasks'),
    # path('your_task', views.Your_List, name='Tasks')
    # path('logged_in')
    # path('user/tasks/<int:id>')

    # path()
]

