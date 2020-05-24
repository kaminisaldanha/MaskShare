from django.db import models

# Create your models here.


class Needer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    immunocompromised = models.BooleanField(default=False)
    mask_collection_preference = models.CharField(max_length=10)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    profile_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
