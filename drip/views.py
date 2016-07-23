from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.decorators import api_view
from drip.drip_serializer import UserSerializer
from drip.models import User
from django.db.models import Q
from dateutil import parser
from drip.tasks import email_send, sms_send
from datetime import datetime
from django.conf import settings
import pdb
from drip.models import REMINDER_MODE

# Create your views here.


class UserView(APIView):
    # pdb.set_trace()

    def get(self, request, format=None):
        users = User.objects.all()
        srlzr = UserSerializer(users, many=True)
        reminder_mode = [{'id': i[0], 'remider_type':i[1]} for i in REMINDER_MODE]
        return Response({'users':srlzr.data, 'reminder_mode':reminder_mode})

    def post(self, request, format=None):
        # pdb.set_trace()
        data = request.data.copy()
        if data:
            srlzr = UserSerializer(data=data)
            if not srlzr.is_valid():
                return Response(srlzr.errors, status=500)
            srlzr.save()
            return Response(srlzr.data)
        return Response('No data provided.', status=400)

    def put(self, request, format=None):
        # pdb.set_trace()
        Q_obj = Q()
        data = request.data.copy()
        for key in data:
            Q_obj |= Q(**{key: data[key]})
        user = User.objects.get(Q_obj)
        srlzr = UserSerializer(user, data=data, partial=True)
        if not srlzr.is_valid():
            return Response(srlzr.errors, status=500)
        srlzr.save()
        return Response(srlzr.data)


def email_reminder(params):
    if not params['user'].email:
        return 'Email id unavailable.'
    email_send.apply_async(
        args=[params['user'].email, params['msg']], eta=params['scheduled_time'])
    # email_send(params['user'].email, params['msg'])
    return 'Email sent successfully.'


def phone_reminder(params):
    if not params['user'].phone:
        return 'Phone number unavailable.'
    if not settings.SMS_DEVICE_ID:
        return 'Sms reminder not available'
    sms_send.apply_async(
        args=[params['user'].phone, params['msg']], eta=params['scheduled_time'])
    # sms_send(params['user'].phone, params['msg'])
    return 'Sms sent successfully'


class SendReminder(APIView):

    def post(self, request, format=None):
        # pdb.set_trace()
        reminder_choice = {1: email_reminder, 2: phone_reminder}
        data = request.data.copy()
        user = User.objects.get(id=data['user'])
        scheduled_time = parser.parse(data['scheduled_time'])
        if scheduled_time <= datetime.now():
            return Response('Invalid Scheduled Time', status=400)
        result = []
        if not data['reminder_type']:
            return Response('No mode of reminder selected.', status=400)
        if not settings.CELERY_USE:
            return Response('Celery not running', status=500)
        for key in data['reminder_type']:
            result.append(reminder_choice.get(key)(
                {'user': user, 'msg': data['msg'], 'scheduled_time': scheduled_time}))
        return Response(result)
