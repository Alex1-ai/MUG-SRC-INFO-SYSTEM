from django.db import models

# Create your models here.
class Src_News(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to='newspics/', default="newspics/mug3_DCcYNyH.jpg")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'src_news'
        verbose_name_plural = 'src_news'

    def __str__(self) -> str:
        return self.title
