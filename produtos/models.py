from django.db import models

class Produto(models.Model):

    nome= models.CharField(max_length=50)
    descricao= models.TextField()
    quantidade = models.IntegerField()

  
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.nome
