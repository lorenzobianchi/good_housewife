from django.db import models
from django.utils import timezone
from django.urls import reverse

class Spesa(models.Model):
    importo = models.DecimalField(max_digits=6, decimal_places=2)
    causale = models.CharField(max_length=100)
    data = models.DateTimeField(default=timezone.now)
    note = models.TextField(null=True, blank=True)
    tipo_spesa = models.ForeignKey('TipoSpesa', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "%s - %s" %(self.importo, self.causale)

    def get_absolute_url(self):
        return reverse('spesa_detail', args=[str(self.id)])

class TipoSpesa(models.Model):
    nome = models.CharField(max_length=100)
    colore_badge = models.CharField(max_length=30)
    spesa_ordinaria = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('tipo_spesa_detail', args=[str(self.id)])
