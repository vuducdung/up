from django.db import models

# Create your models here.
class Paper(models.Model):
    id = models.CharField(primary_key=True, max_length=23)
    title = models.TextField(null=True, blank=True)
    cover_date = models.DateTimeField(auto_now_add=True, blank=True)
    url = models.CharField(max_length=191, null=True)

class University(models.Model):
    name = models.CharField(max_length=191)

class Author(models.Model):
    id = models.BigIntegerField(primary_key=True)
    given_name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    email = models.CharField(max_length=191)
    url = models.CharField(max_length=191)
    university_id = models.ForeignKey(University, on_delete=models.CASCADE)

class Author_Paper(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    paper_id = models.ForeignKey(Paper, on_delete = models.CASCADE)