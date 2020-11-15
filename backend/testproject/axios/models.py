from django.db import models
import jsonfield

# Create your models here.


class FormMaterial(models.Model):
    name = models.CharField(verbose_name='カテゴリー名', max_length=255, null=True, blank=True)
    materials = jsonfield.JSONField(blank=True, null=True)


class FormCategory(models.Model):
    name = models.CharField(verbose_name='カテゴリー名', unique=True, max_length=255)
    items = models.ManyToManyField(FormMaterial)


class FormLabel(models.Model):
    name = models.CharField(verbose_name='フォーム名', unique=True, max_length=255)
    category = models.ForeignKey(FormCategory, on_delete=models.CASCADE)
