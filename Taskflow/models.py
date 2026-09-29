from django.db import models


class Taches(models.Model):
    type_tache = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(max_length=50)
    
    def __str__(self):
        return self.type_tache