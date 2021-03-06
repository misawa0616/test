# Generated by Django 3.1.4 on 2020-12-28 07:54

import common.utilis
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='カテゴリー名')),
                ('materials', models.JSONField(blank=True, encoder=common.utilis.ensure_ascii_false_json_encoder, null=True)),
            ],
        ),
    ]
