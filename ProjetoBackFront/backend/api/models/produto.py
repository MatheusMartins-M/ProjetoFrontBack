import random
import string
from django.db import models
from .base_model import BaseModel
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator

class Produto(BaseModel):
    cod = models.CharField(
        null= False, blank = False, max_length=4,
        validators=[MinLengthValidator(1)],
        help_text="Código do Produto",
        verbose_name="Código"
    )
    nome = models.CharField(
        null=False, blank=False, max_length=10,
        validators=[MinLengthValidator(1)],
        help_text="Nome do item",
        verbose_name="Nome"
    )
    valor = models.FloatField(
        null=False, blank=False, 
        validators=[MinValueValidator(1)],
        help_text="Valor do item",
        verbose_name="Valor"
    )

    def __str__(self):
        return (f"{self.cod} - {self.nome} - R${self.valor}")
    
    def save(self, *args, **kargs):
        if self.cod is None or self.cod == '':
            letters = string.ascii_letters + string.digits
            self.cod = ''.join(random.choice(letters) for i in range(10))
        super().save(*args, **kargs)