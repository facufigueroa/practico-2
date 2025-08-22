from django.db import models

class Persona(models.Model):
    """Model definition for Persona."""

    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    apellido = models.CharField(verbose_name="Apellido", max_length=50)
    edad = models.IntegerField(verbose_name="Edad")

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of Persona."""
        return f"Nombre: {self.nombre} {self.apellido}, Edad: {self.edad}"
