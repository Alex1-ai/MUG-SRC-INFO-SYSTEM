from django.db import models









# Create your models here.
class BillBoard(models.Model):
    title  = models.CharField(max_length=255)
    poster_img = models.ImageField(upload_to='photos/billboard')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    

