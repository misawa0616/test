from rest_framework import serializers
from axios.models import FormMaterial, FormLabel


class FormMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormMaterial
        exclude = ()


class FormLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormLabel
        exclude = ()
