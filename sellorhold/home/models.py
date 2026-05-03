from django.db import models

# Create your models here.

class User(models.Model):
    company_name = models.CharField(max_length=120)
    vest_date = models.DateTimeField("When do your stocks vest?")

    def __str__(self):
        return self.company_name
