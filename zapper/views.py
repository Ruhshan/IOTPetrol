from django.shortcuts import render

from django.http import HttpResponse
from django.views import View


import base64
import cv2
import numpy
import time
from datetime import timedelta, datetime
from .tests import *

from .scan_helpers import *

import json
import os
import random
class ScanView(View):

    def get(self, request):
        return render(request, 'zapper/indexf.html')

    def post(self, request):
        payload1 = request.POST['payload1']
        result1 = process_payload(payload1)
        result2 = process_payload(payload1)
        print(result1)
        print(result2)
        return HttpResponse(result2)
        

class DigitPageView(View):
    def get(self, request):
        digit = str(int(random.random() * 99999999))
        digit = digit.replace('1', ' 1')

        return render(request, 'zapper/digit_page.html', {'digit':digit})

class SwitchPageView(View):
    def get(self, request):
        return render(request, 'zapper/mqttswitch.html')