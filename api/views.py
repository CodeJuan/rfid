# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def auth(request):
    if request.method == 'POST':
        data = request.POST
    else:
        data = request.GET
    username = data.get('username')
    password = data.get('password')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        pass
    else:
        if user.check_password(password):
            return HttpResponse('1')
    return HttpResponse('0')
