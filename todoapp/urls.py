from django.urls import path
from .views import TodoView, delete_post

app_name = 'main'
urlpatterns = [
    path('', TodoView, name = 'index'),
    path('delete/<post_id>', delete_post, name='delete')
]