from django.db import models
from django.contrib.auth import authenticate
from mylab.models import Document



class User(models.Model):
    UserName = models.CharField(max_length=20)
    UserIP = models.CharField(max_length = 20, null=False)
    Email = models.EmailField(primary_key=True, max_length = 50)
    PW = models.CharField(max_length=30)
    
    objects = models.Manager()

    def __str__(self):
        return str(self.UserName) + str(self.Email)

    def is_users_document(self, request, document_pk):
        username = request.session["username"]
        document_developer = Document.objects.get(pk = document_pk)

        if(username == document_developer):
            return True
        return False




        
        


    


    
    

    
# Create your models here.
