from django.db import models

# Create your models here.
class Contacto(models.Model):
	id = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 200, blank = False, null = False)
	apellido = models.CharField(max_length = 198, blank = False, null = False)
	email = models.EmailField()
	consulta = models.TextField(blank = False, null = False)
	Whatsapp = models.IntegerField(blank=False,null = False, help_text='Contact phone number')
	fecha_de_creacion = models.DateField('fecha de creacion', auto_now=True, auto_now_add=False)

	class Meta:
		verbose_name = 'Contacto'
		verbose_name_plural = 'Contactos'
		

	def __str__(self):
		return self.nombre
