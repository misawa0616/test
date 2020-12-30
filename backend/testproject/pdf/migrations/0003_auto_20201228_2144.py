# Generated by Django 3.1.4 on 2020-12-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0002_auto_20201228_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdfmaterial',
            name='name',
        ),
        migrations.AddField(
            model_name='pdfmaterial',
            name='key',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='キー名'),
        ),
        migrations.AddField(
            model_name='pdfmaterial',
            name='max',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]