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


class TestPdfAPIView(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    def get(self, request, *args, **kwargs):
        # Create a file-like buffer to receive PDF data.
        # a = PdfReader('./sample.pdf')
        buffer = io.BytesIO()
        cc = canvas.Canvas(buffer, pagesize=portrait(A4))
        fontname_g = "HeiseiKakuGo-W5"
        pdfmetrics.registerFont(UnicodeCIDFont(fontname_g))
        page = PdfReader('./hello-world.pdf', decompress=False).pages
        pp = pagexobj(page[0])


        # Create the PDF object, using the buffer as its "file."
        cc.doForm(makerl(cc, pp))
        cc.setFont(fontname_g, 24)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        cc.drawString(100, 100, "テスト.")

        # Close the PDF object cleanly, and we're done.
        cc.showPage()
        cc.save()

        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


