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
from pdf.models import PdfMaterial
import io
from pdfrw.toreportlab import makerl
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from pdfrw import PdfReader
from reportlab.pdfgen import canvas
from pdfrw.buildxobj import pagexobj

from rest_framework.authentication import SessionAuthentication
from PyPDF2.pdf import PdfFileReader, PdfFileWriter


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


class TestPDFAPIView(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('POST', 'HEAD')

    def test(self, cc, i, test):
        for i1 in i:
            if i1.get('type') == 3:
                s = ""
                e = ""
                k = ""
                for i2 in i1.get('argument'):
                    if i2.get("key_label") == 'キー':
                        k = i2.get("key_value")
                    if i2.get("key_label") == '開始':
                        s = i2.get("key_value")
                    if i2.get("key_label") == '終了':
                        e = i2.get("key_value")
                for i2 in i1.get('contents'):
                    test_list = []
                    if int(s) == int(e):
                        test_list.append(test.get(k)[int(s)])
                    else:
                        test_list.append(test.get(k)[int(s):int(e)])
                    if i2.get('if_value') in test_list:
                        self.test(cc, i2.get('contents'), test)
            elif i1.get('type') == 2:
                x = ""
                y = ""
                k = ""
                for i2 in i1.get('argument'):
                    if i2.get("key_label") == 'キー':
                        k = i2.get("key_value")
                    if i2.get("key_label") == 'x軸':
                        x = i2.get("key_value")
                    if i2.get("key_label") == 'y軸':
                        y = i2.get("key_value")
                cc.drawString(int(x), int(y), test.get(k))

    def post(self, request, *args, **kwargs):
        fontname_g = "HeiseiKakuGo-W5"
        pdfmetrics.registerFont(UnicodeCIDFont(fontname_g))
        buffer = io.BytesIO()
        cc = canvas.Canvas(buffer)
        cc.setFont(fontname_g, 24)
        reader = PdfFileReader('media/pdf/sample.pdf')
        writer = PdfFileWriter()
        test = {"test1": "test1", "test2": "S2", "test3": "テスト",
                "test4": [
                    {"key_label": "テスト1", "flag": True},
                    {"key_label": "テスト2", "flag": True},
                    {"key_label": "テスト3", "flag": True},
                ]}
        print(request.data['test_list'])
        a = request.data['test_list']
        for i in a:
            self.test(cc, i.get('contents'), test)
        cc.showPage()
        cc.save()
        buffer.seek(0)
        new_pdf = PdfFileReader(buffer)
        existing_page = reader.getPage(0)
        existing_page.mergePage(new_pdf.getPage(0))
        writer.addPage(existing_page)

        new = io.BytesIO()
        writer.write(new)
        new.seek(0)

        output_pdf = open('media/pdf/sample2.pdf', 'wb')
        writer.write(output_pdf)
        output_pdf.close()
        return Response({'detail': _('Successfully confirmed email.')},
                        status=status.HTTP_201_CREATED)
