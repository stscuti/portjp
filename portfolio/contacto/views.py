from django.conf import settings

from django.shortcuts import render, redirect

from django.template.loader import get_template

from django.core.mail import EmailMultiAlternatives

from .forms import ContactoForm

from django.contrib import messages

# Create your views here.
def Home(request):
	return render(request, 'index.html')

def send_email(email):
	context = {'email': email}
	template = get_template('correo.html')
	content = template.render(context)

	email = EmailMultiAlternatives(
            'un correo de prueba',
            'Portfolio Juan Bentos',
            settings.EMAIL_HOST_USER,
            [email]

		)

	email.attach_alternative(content, 'text/html')
	email.send()


def AvisoContacto(request):
	return render(request, 'contacto/avisocontacto.html')



def crearContacto(request):
	if request.method == 'POST':
		
		contacto_form = ContactoForm(request.POST)
		if contacto_form.is_valid():
			email = request.POST.get('email')
			send_email(email)
			contacto_form.save()
			messages.success(request, "Contacto agregado")
			return redirect(Home)
	else:
		contacto_form = ContactoForm()
	return render(request,'contacto/crearcontacto.html',{'contacto_form': contacto_form})





