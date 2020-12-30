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
from PyPDF2 import PdfFileMerger
from reportlab.platypus import Table, TableStyle, Paragraph, SimpleDocTemplate
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from pdf.models import PdfMaterial


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
        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


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
        return FileResponse(new, as_attachment=True, filename='hello.pdf')


class TestPyPDF2APIView2(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    @classmethod
    def motion_purpose_draw(cls, cc, rect_x, text_x, text_width, text_other_width, rect_edge,
                            rect_line_width, initial, s, other_list, temp_list, line_height, paragraph_style,
                            table_format, *args, **kwargs):
        text_list = []
        last_other_flag = False
        s = j = s
        for temp in temp_list:
            if temp in other_list:
                last_other_flag = True
                break
        for i, temp in enumerate(temp_list):
            tep = initial - (j - s) * line_height

            text = Paragraph(temp, style=paragraph_style)
            if temp in other_list:
                last_other_flag = False
                table = Table([[text, "(", ")"]], colWidths=text_other_width)
            else:
                table = Table([[text]], colWidths=text_width)
            table.setStyle(TableStyle(table_format))
            w, h = table.wrap(0, 0)
            text_material = {"label": temp, "position": j - s}
            s -= h / line_height
            if last_other_flag:
                is_valid = s > 0
            else:
                is_valid = s >= 0
            if is_valid:
                text_list.append(text_material)
                table.wrapOn(cc, text_x, tep - h + rect_edge)
                table.drawOn(cc, text_x, tep - h + rect_edge)
                cc.setLineWidth(rect_line_width)
                cc.rect(rect_x, tep, rect_edge, rect_edge, stroke=1, fill=False)
            else:
                if last_other_flag:
                    text = Paragraph(other_list[0], style=paragraph_style)
                    table = Table([[text, "(", ")"]], colWidths=text_other_width)
                    table.setStyle(TableStyle(table_format))
                    w, h = table.wrap(0, 0)
                    text_material = {"label": temp, "position": j - s}
                    text_list.append(text_material)
                    table.wrapOn(cc, text_x, tep - h + rect_edge)
                    table.drawOn(cc, text_x, tep - h + rect_edge)
                    cc.setLineWidth(rect_line_width)
                    cc.rect(rect_x, tep, rect_edge, rect_edge, stroke=1, fill=False)
                break
        return cc, text_list

    @classmethod
    def welfare_equipment_draw(cls, cc, circle_x, text_x, text_width, circle_edge,
                               initial, s, other_list, temp_list, line_height, paragraph_style,
                               table_format, y_adjust, before_rect_x, after_rect_x, rect_edge,
                               rect_line_width, circle_line_width, *args, **kwargs):
        welfare_equipment_list = []
        s = j = s
        for temp in temp_list:
            if temp in other_list:
                continue
            else:
                tep = initial - (j - s) * line_height
                text = Paragraph(temp, style=paragraph_style)
                table = Table([[text]], colWidths=text_width)
                table.setStyle(TableStyle(table_format))
                w, h = table.wrap(0, 0)
                welfare_equipment = {"label": temp, "position": j - s}
                s -= h / line_height
                if s >= 0:
                    welfare_equipment_list.append(welfare_equipment)
                    cc.setLineWidth(circle_line_width)
                    cc.circle(circle_x, tep, circle_edge, stroke=1, fill=True)
                    cc.setLineWidth(rect_line_width)
                    cc.rect(before_rect_x, tep - y_adjust, rect_edge, rect_edge, stroke=1, fill=False)
                    cc.rect(after_rect_x, tep - y_adjust, rect_edge, rect_edge, stroke=1, fill=False)
                    table.wrapOn(cc, text_x, tep - h + y_adjust)
                    table.drawOn(cc, text_x, tep - h + y_adjust)
                else:
                    break
        return cc, welfare_equipment_list

    def get(self, request, *args, **kwargs):
        fontname_g = "HeiseiMin-W3"
        pdfmetrics.registerFont(UnicodeCIDFont(fontname_g))
        reader = PdfFileReader('media/pdf/riyuu-format3.pdf')
        writer = PdfFileWriter()

        buffer = io.BytesIO()
        cc = canvas.Canvas(buffer)
        cc.setFont(fontname_g, 8)
        other_list = ["その他"]
        temp_list = ["トイレまでの移動",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "その他",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り（移乗を含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "その他"
                     ]
        table_format = [
            ('FONT', (0, 0), (-1, -1), fontname_g, 8),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ]
        line_height = 11.9
        normal_paragraph_style = ParagraphStyle(name='Normal', fontName=fontname_g, fontSize=7, leading=line_height)
        text_width = (85,)
        circle_x = 644.5
        text_x = 648.5
        before_rect_x = 747
        after_rect_x = 775.5
        rect_edge = 8
        circle_edge = 3
        rect_line_width = 0.7
        circle_line_width = 1
        initial = 296
        s = 15
        y_adjust = 4
        cc, welfare_equipment_list = self.welfare_equipment_draw(cc, circle_x, text_x, text_width,
                                                                 circle_edge, initial, s, other_list, temp_list,
                                                                 line_height, normal_paragraph_style, table_format,
                                                                 y_adjust, before_rect_x, after_rect_x, rect_edge,
                                                                 rect_line_width, circle_line_width)
        welfare_equipment_material = PdfMaterial.objects.get(key="welfare_equipment")
        welfare_equipment_material.materials = welfare_equipment_list
        welfare_equipment_material.save()
        cc.showPage()
        cc.save()
        buffer.seek(0)
        new_pdf = PdfFileReader(buffer)
        existing_page = reader.getPage(0)
        existing_page.mergePage(new_pdf.getPage(0))
        writer.addPage(existing_page)

        buffer = io.BytesIO()
        cc = canvas.Canvas(buffer)
        cc.setFont(fontname_g, 6)
        line_height = 10.7
        table_format = [
            ('FONT', (0, 0), (-1, -1), fontname_g, 6),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ]
        normal_paragraph_style = ParagraphStyle(name='Normal', fontName=fontname_g, fontSize=6, leading=line_height)
        motion_rect_x = 59
        motion_width = (90,)
        motion_other_width = (18, 70, 3)
        motion_x = 67
        purpose_rect_x = 342
        purpose_width = (85,)
        purpose_other_width = (18, 62, 3)
        purpose_x = 350
        rect_edge = 6.5
        rect_line_width = 0.5
        initial = 477.5
        s = 9
        other_list = ["その他"]
        temp_list = ["トイレまでの移動",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "便器からの立ち座り（移乗を含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "その他"
                     ]
        cc, text_list = self.motion_purpose_draw(cc, motion_rect_x, motion_x, motion_width, motion_other_width,
                                                 rect_edge,  rect_line_width, initial, s, other_list, temp_list,
                                                 line_height, normal_paragraph_style, table_format)
        text_material = PdfMaterial.objects.get(key="toilet_motion")
        text_material.materials = text_list
        text_material.save()
        temp_list = ["トイレまでの移動",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "便器からの立ち座り（移乗を含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "その他"
                     ]
        cc, text_list = self.motion_purpose_draw(cc, purpose_rect_x, purpose_x, purpose_width, purpose_other_width,
                                                 rect_edge,  rect_line_width, initial, s, other_list, temp_list,
                                                 line_height, normal_paragraph_style, table_format)
        text_material = PdfMaterial.objects.get(key="toilet_purpose")
        text_material.materials = text_list
        text_material.save()
        initial = 381.4
        s = 10
        temp_list = ["トイレまでの移動",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "便器からの立ち座り（移乗を含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "その他"
                     ]
        cc, text_list = self.motion_purpose_draw(cc, motion_rect_x, motion_x, motion_width, motion_other_width,
                                                 rect_edge,  rect_line_width, initial, s, other_list, temp_list,
                                                 line_height, normal_paragraph_style, table_format)
        text_material = PdfMaterial.objects.get(key="bath_motion")
        text_material.materials = text_list
        text_material.save()
        temp_list = ["トイレまでの移動",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "便器からの立ち座り（移乗を含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "その他"
                     ]
        cc, text_list = self.motion_purpose_draw(cc, purpose_rect_x, purpose_x, purpose_width, purpose_other_width,
                                                 rect_edge,  rect_line_width, initial, s, other_list, temp_list,
                                                 line_height, normal_paragraph_style, table_format)
        text_material = PdfMaterial.objects.get(key="bath_purpose")
        text_material.materials = text_list
        text_material.save()
        initial = 274.5
        s = 9
        temp_list = ["トイレまでの移動",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "便器からの立ち座り（移乗を含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "その他"
                     ]
        cc, text_list = self.motion_purpose_draw(cc, motion_rect_x, motion_x, motion_width, motion_other_width,
                                                 rect_edge,  rect_line_width, initial, s, other_list, temp_list,
                                                 line_height, normal_paragraph_style, table_format)
        text_material = PdfMaterial.objects.get(key="go_out_motion")
        text_material.materials = text_list
        text_material.save()
        temp_list = ["トイレまでの移動",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "便器からの立ち座り（移乗を含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "その他"
                     ]
        cc, text_list = self.motion_purpose_draw(cc, purpose_rect_x, purpose_x, purpose_width, purpose_other_width,
                                                 rect_edge,  rect_line_width, initial, s, other_list, temp_list,
                                                 line_height, normal_paragraph_style, table_format)
        text_material = PdfMaterial.objects.get(key="go_out_purpose")
        text_material.materials = text_list
        text_material.save()
        initial = 178
        s = 9
        temp_list = ["トイレまでの移動",
                     "トイレ出入口の出入（扉の開閉含む）",
                     "便器からの立ち座り（移乗を含む）",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "便器からの立ち座り",
                     "その他"
                     ]
        cc, text_list = self.motion_purpose_draw(cc, purpose_rect_x, purpose_x, purpose_width, purpose_other_width,
                                                 rect_edge,  rect_line_width, initial, s, other_list, temp_list,
                                                 line_height, normal_paragraph_style, table_format)
        text_material = PdfMaterial.objects.get(key="other_purpose")
        text_material.materials = text_list
        text_material.save()
        cc.showPage()
        cc.save()
        buffer.seek(0)
        new_pdf = PdfFileReader(buffer)
        existing_page = reader.getPage(1)
        existing_page.mergePage(new_pdf.getPage(0))
        writer.addPage(existing_page)

        new = io.BytesIO()
        writer.write(new)
        new.seek(0)

        output_pdf = open('media/pdf/riyuu-format4.pdf', 'wb')
        writer.write(output_pdf)
        output_pdf.close()
        return FileResponse(new, as_attachment=True, filename='hello.pdf')


class TestPyPDF2APIView3(APIView):

    permission_classes = (AllowAny,)
    allowed_methods = ('GET', 'HEAD')

    @classmethod
    def motion_purpose_draw(cls, cc, before_rect_x, after_rect_x, temp_list, input_list,
                            initial, line_height, *args, **kwargs):
        for input_value in input_list:
            for temp in temp_list:
                if temp["label"] == input_value["label"]:
                    tep = initial - temp["position"] * line_height
                    if input_value["before_flag"]:
                        cc.drawString(before_rect_x, tep, "v")
                    if input_value["after_flag"]:
                        cc.drawString(after_rect_x, tep, "v")
                    break
        return cc

    def get(self, request, *args, **kwargs):
        fontname_g = "HeiseiMin-W3"
        pdfmetrics.registerFont(UnicodeCIDFont(fontname_g))
        reader = PdfFileReader('media/pdf/riyuu-format4.pdf')
        writer = PdfFileWriter()
        buffer = io.BytesIO()
        cc = canvas.Canvas(buffer)
        cc.setFont(fontname_g, 11)
        initial = 295
        before_rect_x = 748
        after_rect_x = 776.5
        line_height = 11.9
        input_list = [{'label': '便器からの立ち座り', 'before_flag': True, 'after_flag': False},
                      {'label': 'トイレまでの移動', 'before_flag': False, 'after_flag': True},
                      {'label': 'トイレ出入口の出入（扉の開閉含む）', 'before_flag': True, 'after_flag': False}]
        welfare_equipment_material = PdfMaterial.objects.get(key="welfare_equipment")
        cc = self.motion_purpose_draw(cc, before_rect_x, after_rect_x, welfare_equipment_material.materials,
                                      input_list, initial, line_height)
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
        return FileResponse(new, as_attachment=True, filename='hello.pdf')