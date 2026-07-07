from django.db import models

class profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    full_name = models.CharField(max_length=255)
    email     = models.EmailField(unique=True)   # unique so no duplicate emails
    password  = models.CharField(max_length=255) # stores hashed password
    gender    = models.CharField(max_length=1, choices=GENDER_CHOICES)
    skills    = models.CharField(max_length=255) # stores selected skills as text
    agree     = models.BooleanField(default=False)
    dob       = models.DateField()

    def __str__(self):
      return self.full_name



    