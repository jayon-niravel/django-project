from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 20)

    def __str__(self):
        return self.name