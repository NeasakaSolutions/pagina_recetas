# Email
import os
from dotenv import load_dotenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTPResponseException



def sendMail(html, asunto, para):
    # Configuracion de las variables:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = asunto
    msg['From'] = os.getenv("SMTP_USER")
    msg['To'] = para

    # Configuracion del mensaje
    msg.attach(MIMEText(html, 'html'))

    try:
        # Conexión al servidor SMTP usando los valores del archivo .env
        server = smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT")))
        # Autenticación en el servidor SMTP con usuario y contraseña
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
        # Envío del correo electrónico al destinatario
        server.sendmail(os.getenv("SMTP_USER"), para, msg.as_string())
        # Cierre de la conexión con el servidor SMTP
        server.quit()
    except SMTPResponseException as e:
        print("Error envio mail")

