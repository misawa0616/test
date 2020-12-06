from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import datetime
from django.utils.timezone import make_aware


class TestDatetimeAPIView(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    def get(self, request, *args, **kwargs):
        print(datetime.datetime.now())
        print(datetime.datetime.now(datetime.timezone.utc))
        print(make_aware(datetime.datetime.now()))
        return Response(status=status.HTTP_201_CREATED)
