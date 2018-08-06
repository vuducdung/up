from django.shortcuts import render
from .models import Author, University
from django.http import HttpResponse




# Create your views here.
def author(request):
    authors = Author.objects.select_related('university_id')
    return render(request, 'pages/author.html', {'authors':authors})


def deleteAuthor(request,id):
    author = Author.objects.get(id=id)
    author.delete()
    authors = Author.objects.select_related('university_id')
    return render(request, 'pages/author.html', {'authors': authors})

from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts

def GenerateRandomUserView(request,id):
    author = Author.objects.get(id=id)
    author.delete()
    authors = Author.objects.select_related('university_id')
    return render(request, 'pages/author.html', {'authors': authors})