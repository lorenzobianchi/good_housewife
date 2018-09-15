from django.db import models
from django.utils import timezone

class Spesa(models.Model):
    importo = models.DecimalField(max_digits=6, decimal_places=2)
    causale = models.CharField(max_length=100)
    data = models.DateTimeField(default=timezone.now)
    note = models.TextField(null=True, blank=True)
    spesa_ordinaria = models.BooleanField(default=False)
    categoria = models.ForeignKey('TipoSpesa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s - %s" %(self.importo, self.causale)

class TipoSpesa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
