from django.db import models

# Create your models here.

'''This is a one-to-many relationship where there is one Giver that can have multiple masks.
All Masks that the Giver enters should be put in the Mask table. If a Mask is collected
by a Needer, it can be deleted from the Mask table. If a Giver chooses to delete
their profile, all of their masks will be deleted from the Mask table. '''


class Giver(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    profile_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Mask(models.Model):
    mask_giver = models.ForeignKey(Giver, on_delete=models.CASCADE)
    mask_type = models.CharField(max_length=20)
    time_of_entry = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.mask_type
