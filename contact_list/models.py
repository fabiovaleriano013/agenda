from django.db import models

class Contact(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    categoria = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)

    def __str__(self):
        return f"{self.nome} - {self.sobrenome}"