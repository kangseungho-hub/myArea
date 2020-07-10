from django.db import models


class User(models.Model):
    UserName = models.CharField(max_length=20, )
    Email = models.EmailField(primary_key=True, max_length = 50)
    PW = models.CharField(max_length=30)

    def __str__(self):
        return str(self.UserName) + str(self.Email)

    
    

    
# Create your models here.
