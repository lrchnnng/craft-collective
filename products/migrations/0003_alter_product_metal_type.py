# Generated by Django 3.2.25 on 2024-05-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20240501_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='metal_type',
            field=models.CharField(blank=True, choices=[('gold', 'Gold'), ('silver', 'Silver'), ('rosegold', 'Rose Gold')], default='silver', max_length=10, null=True),
        ),
    ]
