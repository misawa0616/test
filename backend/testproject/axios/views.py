from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from axios.models import FormMaterial
from rest_framework.authentication import SessionAuthentication
from json import JSONEncoder
import json
import logging
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class TestAxiosAPIView(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, )
    permission_classes = (IsAuthenticated,)
    allowed_methods = ('POST', 'HEAD')

    def post(self, request, *args, **kwargs):
        print(request)
        a = FormMaterial(
            name="a",
            materials={
                "a": {
                    "a": "ありがとうねー"
                }
            })
        a.save()
        return Response({'detail': _('Successfully confirmed email.')},
                        status=status.HTTP_201_CREATED)


class TestLogAPIView(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    def get(self, request, *args, **kwargs):
        return Response({'detail': _('Successfully confirmed email.')},
                        status=status.HTTP_201_CREATED)
