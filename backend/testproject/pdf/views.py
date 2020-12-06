import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
from rest_framework.response import Response
from rest_framework import status
from PyPDF2.pdf import PdfFileReader, PdfFileWriter


class TestPdfrwAPIView(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    def get(self, request, *args, **kwargs):
        fontname_g = "HeiseiKakuGo-W5"
        pdfmetrics.registerFont(UnicodeCIDFont(fontname_g))
        buffer = io.BytesIO()
        cc = canvas.Canvas(buffer)
        page = PdfReader('media/pdf/sample.pdf', decompress=False).pages
        pp = pagexobj(page[0])
        cc.doForm(makerl(cc, pp))
        cc.setFont(fontname_g, 24)
        cc.drawString(0, 820, "テスト")
        cc.showPage()
        cc.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=False, filename='hello.pdf')


class TestPyPDF2APIView(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    def get(self, request, *args, **kwargs):
        fontname_g = "HeiseiKakuGo-W5"
        pdfmetrics.registerFont(UnicodeCIDFont(fontname_g))
        buffer = io.BytesIO()
        cc = canvas.Canvas(buffer)
        reader = PdfFileReader('media/pdf/sample.pdf')
        existing_page = reader.getPage(0)
        cc.setFont(fontname_g, 24)
        cc.drawString(0, 820, "テスト")
        cc.showPage()
        cc.save()
        buffer.seek(0)
        new_pdf = PdfFileReader(buffer)
        existing_page.mergePage(new_pdf.getPage(0))
        writer = PdfFileWriter()
        writer.addPage(existing_page)
        new = io.BytesIO()
        writer.write(new)
        new.seek(0)
        return FileResponse(new, as_attachment=False, filename='hello.pdf')
