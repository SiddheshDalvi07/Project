# Generated by Django 5.0.4 on 2024-05-09 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_alter_product_pimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimage',
            field=models.ImageField(upload_to='images'),
        ),
    ]