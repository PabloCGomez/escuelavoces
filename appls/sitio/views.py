from django.shortcuts import render
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
# Create your views here.
def home(request):
    
            
    return render(request, "home.html")




def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        if not nombre or not email or not mensaje:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, "contacto.html")

        # -------------------------
        # 1️⃣ Correo interno (ustedes)
        # -------------------------
        asunto_admin = f"Nuevo contacto - {nombre}"

        cuerpo_admin = f"""
Nombre: {nombre}
Email: {email}

Mensaje:
{mensaje}
"""

        try:
            EmailMessage(
                subject=asunto_admin,
                body=cuerpo_admin,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=["site.escuelavoces@gmail.com"],
                reply_to=[email],
            ).send()

            # -------------------------
            # 2️⃣ Correo HTML al usuario
            # -------------------------
            asunto_user = "Gracias por contactarnos 🎶"

            cuerpo_html = f"""
            <html>
            <body style="font-family: Arial, sans-serif; background-color:#f4f6f8; padding:20px;">
              <table width="100%" cellspacing="0" cellpadding="0">
                <tr>
                  <td align="center">
                    <table width="600" style="background:#ffffff; border-radius:10px; padding:30px;">
                      
                      <tr>
                        <td align="center">
                          <h2 style="color:#4a6cf7;">Escuela Voces</h2>
                        </td>
                      </tr>

                      <tr>
                        <td>
                          <p style="font-size:16px;">Hola <strong>{nombre}</strong>,</p>

                          <p style="font-size:15px; color:#333;">
                            Gracias por escribirnos 💙  
                            Hemos recibido tu mensaje correctamente.
                          </p>

                          <p style="font-size:15px; color:#333;">
                            Nuestro equipo se pondrá en contacto contigo a la brevedad.
                          </p>

                          <p style="font-size:15px; color:#333;">
                            🎵 <strong>Pronto te contactaremos.</strong>
                          </p>

                          <br>

                          <p style="font-size:14px; color:#777;">
                            Saludos cordiales,<br>
                            <strong>Equipo Escuela Voces</strong>
                          </p>
                        </td>
                      </tr>

                      <tr>
                        <td align="center" style="padding-top:20px;">
                          <p style="font-size:12px; color:#999;">
                            Este correo es automático, por favor no respondas.
                          </p>
                        </td>
                      </tr>

                    </table>
                  </td>
                </tr>
              </table>
            </body>
            </html>
            """

            email_user = EmailMessage(
                subject=asunto_user,
                body=cuerpo_html,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            email_user.content_subtype = "html"  # 👈 CLAVE
            email_user.send()

            messages.success(request, "Mensaje enviado correctamente ✅")

        except Exception as e:
            messages.error(request, "Error al enviar el mensaje ❌")
            print(e)

    return render(request, "contacto.html")


    



def quienes_somos(request):
    return render(request, "quienes_somos.html")
    