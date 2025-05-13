from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactoForm
from django.contrib import messages

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            celular = form.cleaned_data['celular']
            mensaje = form.cleaned_data['mensaje']

            asunto = f"Consulta de cliente desde la web - {nombre}"
            cuerpo = f"Nombre: {nombre}\nEmail: {email}\nCelular: {celular}\nMensaje:\n{mensaje}"
            destinatario = settings.EMAIL_DESTINATARIO  # Usaremos una configuración en settings.py

            try:
                send_mail(asunto, cuerpo, settings.DEFAULT_FROM_EMAIL, [destinatario])
                messages.success(request, 'Tu mensaje ha sido enviado. Te contactaremos pronto.')
                return redirect('contacto')  # Redirige a la misma página con un mensaje de éxito
            except Exception as e:
                messages.error(request, f'Hubo un error al enviar el mensaje: {e}')
                return render(request, 'contacto.html', {'form': form})
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})

# Create your views here.
def render_home(request):
    return render(request, 'home.html')

