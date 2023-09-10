from django.db import models
from api.account.models import User
# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self):
        return self.name




class Candidate(models.Model):
    name = models.CharField(max_length=35)
    image = models.ImageField(upload_to='photos/candidate_pics')
    votes = models.IntegerField(default=0)  # Field to store the vote count
    department = models.CharField(max_length=17)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    # manifesto = models.TextField()
   
    def __str__(self):
        return f"{self.name} - {self.position}"


class Vote(models.Model):
    email = models.EmailField(max_length=255)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    voted_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     unique_together = ('user', 'candidate')
        
    def __str__(self):
        return f"{self.email} voted for {self.candidate.name}"
    
    