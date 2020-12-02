#! /usr/bin/python
#
#   pdf_overwrite_plural.py
#
#                       Jan/17/2019
#
# ------------------------------------------------------------------
import sys
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import portrait
# ------------------------------------------------------------------
def page_1_proc(cc,pp,fontname_g):
    cc.doForm(makerl(cc, pp))
    cc.setFont(fontname_g,24)
    cc.drawString(400,800,"おはよう")
    cc.drawString(400,700,"１ページ目")
    cc.drawString(400,600,"Good Morning")
    cc.showPage()
#
# ------------------------------------------------------------------
def page_2_proc(cc,pp,fontname_g):
    cc.doForm(makerl(cc, pp))
    cc.setFont(fontname_g,24)
    cc.drawString(400,800,"こんにちは")
    cc.drawString(400,700,"２ページ目")
    cc.drawString(400,600,"Hello")
    cc.showPage()
#
# ------------------------------------------------------------------
def page_3_proc(cc,pp,fontname_g):
    cc.doForm(makerl(cc, pp))
    cc.setFont(fontname_g,24)
    cc.drawString(400,800,"今晩は")
    cc.drawString(400,700,"３ページ目")
    cc.drawString(400,600,"Good Evening")
    cc.showPage()
#
# ------------------------------------------------------------------
sys.stderr.write ("*** 開始 ***\n")
file_in = sys.argv[1]
file_out = sys.argv[2]
sys.stderr.write(file_in + "\n")
sys.stderr.write(file_out + "\n")
#

cc = canvas.Canvas(file_out,pagesize=portrait(A4))
fontname_g = "HeiseiKakuGo-W5"
pdfmetrics.registerFont (UnicodeCIDFont (fontname_g))
#
page = PdfReader(file_in,decompress=False).pages
sys.stderr.write("len(page) = %d\n" % len(page))
#
pp = pagexobj(page[0])
page_1_proc(cc,pp,fontname_g)
#
# pp = pagexobj(page[1])
# page_2_proc(cc,pp,fontname_g)
# #
# pp = pagexobj(page[2])
# page_3_proc(cc,pp,fontname_g)
#
cc.save()
#
sys.stderr.write ("*** 終了 ***\n")
# ------------------------------------------------------------------