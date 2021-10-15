from django.db import models

# Create your models here.

class Independent(models.Model):
    name = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    birth = models.DateField()
    age = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.name