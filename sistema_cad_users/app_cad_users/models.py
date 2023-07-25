from django.db import models

class Users(models.Model):
    id_user = models.AutoField(primary_key=True) #Cria um campo númerico para identificar o usuario
    name = models.TextField(max_length=255)
    age = models.IntegerField()