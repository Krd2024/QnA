# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from aiosmtplib import SMTP
# import asyncio
from decouple import config

#
from django.core.mail import EmailMessage

EMAIL = config("EMAIL_HOST_USER")
PWD = config("EMAIL_HOST_PASSWORD")


#  =================================================================
def send_mail_(subject, to, message):
    email = EmailMessage(
        subject=subject,
        body="1",
        from_email=EMAIL,
        to=[to],
        headers={"Content-Type": 'text/html; charset="utf-8"'},
    )

    # Прикрепите файл к письму
    message.seek(0)
    email.attach("image.jpg", message.read(), message.content_type)

    # Отправьте письмо
    email.send()


print("Email sent with the image attachment.")

# =================================================================
# async def send_mail_(subject, to, msg):
#     message = MIMEMultipart()
#     message["From"] = EMAIL
#     message["To"] = to
#     message["Subject"] = subject
#     # message.attach(MIMEText(f"<html><body>{msg}</body></html>", "html", "utf-8"))
#     message.attach(MIMEMultipart(msg))

#     smtp_client = SMTP(hostname="smtp.yandex.ru", port=465, use_tls=True)

#     async with smtp_client:
#         await smtp_client.login(EMAIL, PWD)
#         await smtp_client.send_message(message)
#     print("ушло")
