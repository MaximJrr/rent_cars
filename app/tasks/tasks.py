import smtplib

from pydantic import EmailStr

from app.config import settings
from app.tasks.celery_app import celery
from app.tasks.email_templates import (
    create_new_car_template,
    create_rent_confirmation_template,
)


@celery.task
def send_rent_confirmation_email(rent: dict, email_to: EmailStr):
    msg_content = create_rent_confirmation_template(rent, email_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)


@celery.task
def send_new_car_message_email(car: dict, *emails_to: EmailStr):
    msg_content = create_new_car_template(car, *emails_to)

    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
