from django.urls import path
from . import views

urlpatterns = [
    path('',views.author, name='author'),
    path('author/<int:id>/',views.deleteAuthor, name='delete'),
]