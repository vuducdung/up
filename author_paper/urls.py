from django.urls import path
from . import views

urlpatterns = [
    path('',views.author, name='author'),
    path('test/',views.author, name=''),
    path('author/<int:id>/',views.deleteAuthor, name='delete'),
]