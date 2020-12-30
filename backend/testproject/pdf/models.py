from django.db import models
from common.utilis import ensure_ascii_false_json_encoder


class PdfMaterial(models.Model):
    key = models.CharField(verbose_name='キー名', max_length=255, null=True, blank=True)
    materials = models.JSONField(blank=True, null=True, encoder=ensure_ascii_false_json_encoder)
    max = models.IntegerField()
