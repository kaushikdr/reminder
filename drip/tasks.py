from celery import task
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.query import QuerySet
import pdb

import requests
import json


@task
def email_send(to_email, msg):
    # pdb.set_trace()°
    if not (isinstance(to_email, list) or isinstance(to_email, QuerySet)):
        to_email = [to_email]

    send_mail('Your Reminder from Remind Me Later', msg,
              settings.DEFAULT_FROM_EMAIL, to_email)


@task
def sms_send(to_phone, msg):
    url = "http://smsgateway.me/api/v3/messages/send"
    data = {"email": "kaushik06101992@gmail.com", "password": "parag123",
            "device": settings.SMS_DEVICE_ID, "number": to_phone, "message": msg}
    resp = requests.post(url, data=data)
    return resp.json()
