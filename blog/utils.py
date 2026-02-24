from django.conf import settings
from django.core.mail import send_mail


def send_email_tu_user(mail: str, subject: str, message: str) ->None:
    """Функция для отправки писем.
    Если в settings.py не настроен доступ к EMAIL_HOST_USER и EMAIL_HOST_PASSWORD, работа сервиса не прервётся."""
    try:
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [mail])
    except Exception as e:
        print(e)
