# Generated by Django 2.2.4 on 2020-02-14 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0007_auto_20200214_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Catalog.Category', verbose_name='Type of Honey'),
        ),
    ]