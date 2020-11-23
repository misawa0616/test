from django.db import models
import jsonfield
from json import JSONEncoder
# from django_mysql.models import JSONField

# Create your models here.


def ensure_ascii_false_json_encoder(skipkeys, ensure_ascii,
                                check_circular, allow_nan, indent,
                                separators, default, sort_keys):
    return JSONEncoder(skipkeys=skipkeys, ensure_ascii=False,
                       check_circular=check_circular, allow_nan=allow_nan, indent=indent,
                       separators=separators, default=default, sort_keys=sort_keys)


class FormMaterial(models.Model):
    name = models.CharField(verbose_name='カテゴリー名', max_length=255, null=True, blank=True)
    materials = jsonfield.JSONField(blank=True, null=True, encoder_class=ensure_ascii_false_json_encoder)


class FormCategory(models.Model):
    name = models.CharField(verbose_name='カテゴリー名', unique=True, max_length=255)
    items = models.ManyToManyField(FormMaterial)


class FormLabel(models.Model):
    name = models.CharField(verbose_name='フォーム名', unique=True, max_length=255)
    category = models.ForeignKey(FormCategory, on_delete=models.CASCADE)
