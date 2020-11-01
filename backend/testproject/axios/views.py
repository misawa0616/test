from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from django.utils.translation import ugettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class TestAxiosAPIView(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    def get(self, request, *args, **kwargs):
        return Response({'detail': _('Successfully confirmed email.')},
                        status=status.HTTP_201_CREATED)
