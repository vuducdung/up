from django.shortcuts import render
from .models import Author, University
from django.http import HttpResponse
from django_ajax.decorators import ajax



# Create your views here.
def author(request):
    authors = Author.objects.select_related('university_id')
    return render(request, 'pages/author.html', {'authors':authors})


def deleteAuthor(request,id):
    author = Author.objects.get(id=id)
    author.delete()
    authors = Author.objects.select_related('university_id')
    return render(request, 'pages/author.html', {'authors': authors})

