# Generated by Django 2.1.7 on 2019-05-11 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_field_tweaks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.CharField(db_index=True, editable=False, max_length=100, verbose_name='product ID'),
        ),
    ]