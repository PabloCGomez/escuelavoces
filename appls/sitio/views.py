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
        telefono = request.POST.get("telefono")

        if not nombre or not email or not mensaje:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, "contacto.html")

        # -------------------------
        # 1️⃣ Correo interno (ustedes)
        # -------------------------
        asunto_admin = f"Nuevo contacto - {nombre}"

        cuerpo_admin = f"""
                          <!DOCTYPE html>
                          <html lang="es">
                          <head>
                            <meta charset="UTF-8">
                          </head>
                          <body style="font-family: Arial, sans-serif;">
                            <p><strong>Hola equipo Escuela Voces,</strong></p>

                            <p>Se ha recibido un nuevo mensaje desde el formulario de contacto:</p>

                            <ul>
                              <li><strong>Nombre:</strong> {nombre}</li>
                              <li><strong>Email:</strong> {email}</li>
                              <li><strong>Teléfono:</strong> {telefono}</li>
                            </ul>

                            <p>Por favor, revisar y responder a la brevedad.</p>

                            <p>Saludos,<br>
                            Sistema Web Escuela Voces</p>
                          </body>
                          </html>
                          """
    
        email_msg = EmailMessage(
                subject=asunto_admin,
                body=cuerpo_admin,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[
                    "site.escuelavoces@gmail.com",
                    "direccion@escuelavoces.cl"
                ],
                reply_to=[email],
            )
        email_msg.content_subtype = "html"
        email_msg.send()


        # -------------------------
        # 2️⃣ Correo HTML al usuario
        # -------------------------
        asunto_user = "Gracias por contactarnos "
        cuerpo_html = f"""
            <!DOCTYPE html>
            <html lang="es">
                
                      <body style="margin:0; padding:0; font-family: Arial, sans-serif; background-color:#f4f6f8;">
                        <table width="100%" cellpadding="0" cellspacing="0" style="padding:20px 0;">
                          <tr>
                            <td align="center">

                    ```
                          <!-- CONTENEDOR -->
                          <table width="600" cellpadding="0" cellspacing="0"
                                style="background-color:#ffffff; border-radius:12px; padding:30px; box-shadow:0 4px 12px rgba(0,0,0,0.08);">

                            <!-- HEADER -->
                            <tr>
                            
                              <td align="center" style="padding-bottom:20px;">
                                <img src="https://escuelavoces.cl/static/img/castillo2.png"
                                      width="90"
                                      alt="Escuela Voces"
                                      style="display:block; margin-bottom:10px;">

                                  <h2 style="margin:0; color:#E53935; font-size:26px;">
                                    Escuela de Lenguaje Voces
                                  </h2>
    
                                
                                
                                <p style="margin:8px 0 0; color:#666; font-size:14px;">
                                  Educación con amor, inclusión y excelencia
                                </p>
                              </td>
                            </tr>

                            <!-- CONTENIDO -->
                            <tr>
                              <td style="color:#333; font-size:15px; line-height:1.6;">
                                <p>Hola <strong>{nombre}</strong>,</p>

                                <p>
                                  💛 Gracias por escribirnos.  
                                  Hemos recibido tu mensaje correctamente y queremos contarte que ya está en manos de nuestro equipo.
                                </p>

                                <p>
                                  Nos pondremos en contacto contigo a la brevedad para entregarte toda la información que necesites.
                                </p>

                                <p style="background-color:#fff3e0; padding:15px; border-radius:8px; text-align:center;">
                                  <strong>¡Gracias por confiar en Escuela Voces!</strong>
                                </p>

                                <p style="margin-top:30px;">
                                  Con cariño,<br>
                                  <strong>Equipo Escuela Voces</strong>
                                </p>
                              </td>
                            </tr>

                            <!-- FOOTER -->
                            <tr>
                              <td align="center" style="padding-top:25px;">
                                <p style="font-size:12px; color:#999;">
                                  Este correo es automático, por favor no respondas a este mensaje. Cel +56 9 3711 3816
                                </p>
                              </td>
                            </tr>

                          </table>

                        </td>
                      </tr>
                    </table>
                    ```

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
    
    return render(request, "contacto.html")


    



def quienes_somos(request):
    return render(request, "quienes_somos.html")
    