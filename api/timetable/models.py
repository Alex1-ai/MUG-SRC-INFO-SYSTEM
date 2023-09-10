from django.db import models

# Create your models here.
class MugDepartment(models.Model):
    departmentName = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) :
        return self.departmentName
# Create your models here.
class Timetable(models.Model):
    name = models.CharField(max_length=45)
    timetableDoc = models.FileField(upload_to='documents/')
    department = models.ForeignKey(MugDepartment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     verbose_name = 'profile'
    #     verbose_name_plural = 'profiles'
    def __str__(self):
        return f"{self.name}"