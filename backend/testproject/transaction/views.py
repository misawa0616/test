from rest_framework.response import Response
from rest_framework import status
from axios.serializers import FormMaterialSerializer, FormLabelSerializer
from rest_framework.views import APIView
from django.db import transaction
import logging

logger = logging.getLogger('django')


class TestTransactionAPIView(APIView):

    @transaction.atomic
    def get(self, request, *args, **kwargs):
        sid = transaction.savepoint()
        request_data_1 = {
            "name": "b",
            "materials": {
                "b": {
                    "b": "ありがとうねー"
                }
            }
        }
        b = FormMaterialSerializer(data=request_data_1)
        if b.is_valid():
            b.save()
        else:
            transaction.savepoint_rollback(sid)
            logger.info(b.errors)
            return Response({'detail': b.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        request_data_2 = {
            "name": "c"
        }
        c = FormLabelSerializer(data=request_data_2)
        if c.is_valid():
            c.save()
        else:
            transaction.savepoint_rollback(sid)
            logger.info(c.errors)
            return Response({'detail': c.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        transaction.savepoint_commit(sid)
        return Response({'detail': 'Successfully confirmed email.'},
                        status=status.HTTP_201_CREATED)
