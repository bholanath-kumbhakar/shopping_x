# Generated by Django 4.1.2 on 2022-10-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
