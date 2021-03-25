from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
	class Meta:
		model = Contacto
		fields = ['nombre', 'apellido', 'email', 'consulta', 'Whatsapp']