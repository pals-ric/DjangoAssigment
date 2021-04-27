from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')


class Candidate(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    candidate_id = models.IntegerField(max_length=10)

    def __str__(self):
        return self.first_name
