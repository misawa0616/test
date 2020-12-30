from django.db import models
import jsonfield
# from django_mysql.models import JSONField
from common.utilis import ensure_ascii_false_json_encoder
# Create your models here.


class FormMaterial(models.Model):
    name = models.CharField(verbose_name='カテゴリー名', max_length=255, null=True, blank=True)
    materials = models.JSONField(blank=True, null=True, encoder=ensure_ascii_false_json_encoder)


class FormCategory(models.Model):
    name = models.CharField(verbose_name='カテゴリー名', unique=True, max_length=255)
    items = models.ManyToManyField(FormMaterial)


class FormLabel(models.Model):
    name = models.CharField(verbose_name='フォーム名', unique=True, max_length=255)
    category = models.ForeignKey(FormCategory, on_delete=models.CASCADE)
